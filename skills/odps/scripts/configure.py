#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import sys

CONFIG_FILE = os.path.expanduser('~/.odps_config.json')
DEFAULT_ENDPOINT = 'http://service-all.ali-sg-lazada.odps.aliyun-inc.com/api'

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    print(f"Configuration saved to {CONFIG_FILE}")

def prompt(msg, default=None):
    if default:
        user_input = input(f"{msg} [{default}]: ").strip()
        return user_input if user_input else default
    else:
        return input(f"{msg}: ").strip()

def main():
    print("=== ODPS Configuration Wizard ===")
    current = load_config()
    
    access_id = prompt("Access ID", current.get('access_id'))
    
    mask = "******" if current.get('secret_access_key') else None
    secret_key = prompt("Secret Access Key", mask)
    if secret_key == "******":
        secret_key = current.get('secret_access_key')
        
    project = prompt("Project Name (Development Project)", current.get('project'))
    endpoint = prompt("Endpoint", current.get('endpoint') or DEFAULT_ENDPOINT)
    
    config = {
        'access_id': access_id,
        'secret_access_key': secret_key,
        'project': project,
        'endpoint': endpoint
    }
    
    save_config(config)

if __name__ == '__main__':
    main()

