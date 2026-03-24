#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
import os
import sys
import csv
import tempfile
from odps import ODPS

# 配置文件路径
CONFIG_FILE = os.path.expanduser('~/.odps_config.json')

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def get_odps_client(args):
    config = load_config()
    
    access_id = os.environ.get('ODPS_ACCESS_ID') or config.get('access_id')
    secret_key = os.environ.get('ODPS_SECRET_ACCESS_KEY') or config.get('secret_access_key')
    project = args.project or os.environ.get('ODPS_PROJECT') or config.get('project')
    endpoint = os.environ.get('ODPS_ENDPOINT') or config.get('endpoint') or 'http://service-all.ali-sg-lazada.odps.aliyun-inc.com/api'
    
    if not access_id or not secret_key or not project:
        print("Error: Missing ODPS configuration. Please run 'run.sh configure.py' first.", file=sys.stderr)
        sys.exit(1)
        
    return ODPS(access_id, secret_key, project, endpoint=endpoint)

def is_safe_path(path):
    """
    Validate if the output path is safe to write to.
    Allowed paths:
    1. Inside current working directory (Project Root)
    2. Inside system temp directory
    """
    abs_path = os.path.abspath(path)
    
    # 1. Check Current Working Directory
    cwd = os.path.abspath(os.getcwd())
    if abs_path.startswith(cwd):
        return True
        
    # 2. Check Temp Directory
    temp_dir = os.path.abspath(tempfile.gettempdir())
    # On macOS, temp dir might be /var/folders/..., which is a symlink to /private/var/folders/...
    # So we resolve real paths for comparison
    real_path = os.path.realpath(abs_path)
    real_temp = os.path.realpath(temp_dir)
    
    if real_path.startswith(real_temp):
        return True
        
    # Special handling for /tmp explicitly (common on Unix-likes even if gettempdir is different)
    if real_path.startswith(os.path.realpath('/tmp')):
        return True

    return False

def run_sql(o, sql, output_file=None):
    print(f"🚀 Submitting SQL to project: {o.project}", file=sys.stderr)
    
    # 自动添加 settings
    hints = {
        'odps.sql.allow.fullscan': 'true',
        'odps.sql.submit.mode': 'script'
    }
    
    try:
        # 执行 SQL
        instance = o.run_sql(sql, hints=hints)
        print(f"✅ Instance created: {instance.id}", file=sys.stderr)
        print(f"🔗 LogView: {instance.get_logview_address()}", file=sys.stderr)
        print("⏳ Waiting for completion...", file=sys.stderr)
        
        instance.wait_for_success()
        
        # 确定输出目标
        if output_file:
            # 安全检查
            if not is_safe_path(output_file):
                raise ValueError(f"Unsafe output path: {output_file}. \nAllowed locations: Current directory ({os.getcwd()}) or Temp directory ({tempfile.gettempdir()}).")

            # 确保目录存在
            output_dir = os.path.dirname(os.path.abspath(output_file))
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            f_out = open(output_file, 'w', newline='', encoding='utf-8')
            print(f"💾 Writing results to: {output_file}", file=sys.stderr)
        else:
            f_out = sys.stdout

        try:
            # 获取结果 (PyODPS 会自动处理 Tunnel)
            with instance.open_reader() as reader:
                writer = csv.writer(f_out)
                
                # 获取 schema
                columns = [col.name for col in reader.schema.columns]
                writer.writerow(columns)
                
                count = 0
                for record in reader:
                    writer.writerow(record.values)
                    count += 1
        finally:
            if output_file and f_out:
                f_out.close()
                
        print(f"\n✨ Done. {count} records retrieved.", file=sys.stderr)
        if output_file:
             print(f"✅ Results saved to {output_file}", file=sys.stderr)
        
    except Exception as e:
        print(f"\n❌ Execution failed: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='ODPS SQL Query Tool')
    parser.add_argument('--sql', required=True, help='SQL statement to execute')
    parser.add_argument('--project', help='Override project name')
    parser.add_argument('--output', '-o', help='Output file path (CSV format). Must be in current directory or temp directory.')
    
    args = parser.parse_args()
    
    o = get_odps_client(args)
    run_sql(o, args.sql, args.output)

if __name__ == '__main__':
    main()
