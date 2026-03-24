#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programmatic AK Configuration Tool for ODPS

This script allows Claude Code to configure ODPS credentials programmatically
when users provide their Access Key information directly in conversation.
"""
import json
import os
import sys
import argparse

CONFIG_FILE = os.path.expanduser('~/.odps_config.json')
DEFAULT_ENDPOINT = 'http://service-all.ali-sg-lazada.odps.aliyun-inc.com/api'

def load_config():
    """Load existing configuration from file."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load existing config: {e}", file=sys.stderr)
    return {}

def save_config(config):
    """Save configuration to file."""
    try:
        # Ensure config directory exists
        config_dir = os.path.dirname(CONFIG_FILE)
        if config_dir and not os.path.exists(config_dir):
            os.makedirs(config_dir, mode=0o700)

        # Write config file with secure permissions
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)

        # Set secure file permissions (owner read/write only)
        os.chmod(CONFIG_FILE, 0o600)

        print(f"✅ Configuration saved to {CONFIG_FILE}")
        return True
    except Exception as e:
        print(f"❌ Failed to save configuration: {e}", file=sys.stderr)
        return False

def validate_config(config):
    """Validate that required configuration fields are present."""
    required_fields = ['access_id', 'secret_access_key', 'project']
    missing_fields = [field for field in required_fields if not config.get(field)]

    if missing_fields:
        print(f"❌ Error: Missing required fields: {', '.join(missing_fields)}", file=sys.stderr)
        return False

    return True

def setup_ak(access_id, secret_key, project, endpoint=None):
    """
    Programmatically configure ODPS Access Key credentials.

    Args:
        access_id: ODPS Access ID
        secret_key: ODPS Secret Access Key
        project: ODPS Project Name (should be development project)
        endpoint: Optional custom endpoint URL

    Returns:
        bool: True if configuration was successful
    """
    # Load existing config to preserve other settings
    config = load_config()

    # Update with new credentials
    config['access_id'] = access_id.strip()
    config['secret_access_key'] = secret_key.strip()
    config['project'] = project.strip()
    config['endpoint'] = (endpoint or config.get('endpoint') or DEFAULT_ENDPOINT).strip()

    # Validate configuration
    if not validate_config(config):
        return False

    # Save configuration
    if save_config(config):
        print("\n📋 Configuration Summary:")
        print(f"   Access ID: {config['access_id']}")
        print(f"   Secret Key: {'*' * min(len(config['secret_access_key']), 20)}")
        print(f"   Project: {config['project']}")
        print(f"   Endpoint: {config['endpoint']}")
        print("\n✨ ODPS credentials configured successfully!")
        print("\n💡 You can now run queries using:")
        print("   ./run.sh query.py --sql \"SELECT * FROM your_table LIMIT 10\"")
        return True

    return False

def main():
    parser = argparse.ArgumentParser(
        description='Programmatically configure ODPS Access Key credentials',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Configure with all required parameters
  %(prog)s --access-id YOUR_AK_ID --secret-key YOUR_AK_SECRET --project your_project_dev

  # Configure with custom endpoint
  %(prog)s --access-id YOUR_AK_ID --secret-key YOUR_AK_SECRET --project your_project_dev \\
    --endpoint http://custom.endpoint.com/api

  # Show current configuration
  %(prog)s --show

Notes:
  - The project should be a development project (usually ends with '_dev')
  - Configuration is saved to ~/.odps_config.json
  - File permissions are automatically set to 600 (owner read/write only)
        """
    )

    parser.add_argument('--access-id', help='ODPS Access ID')
    parser.add_argument('--secret-key', help='ODPS Secret Access Key')
    parser.add_argument('--project', help='ODPS Project Name (development project)')
    parser.add_argument('--endpoint', help='ODPS Endpoint URL (optional)')
    parser.add_argument('--show', action='store_true', help='Show current configuration')

    args = parser.parse_args()

    # Handle --show flag
    if args.show:
        config = load_config()
        if not config:
            print("No configuration found. Run with --access-id, --secret-key, and --project to configure.")
            sys.exit(1)

        print("\n📋 Current ODPS Configuration:")
        print(f"   Access ID: {config.get('access_id', 'Not configured')}")
        print(f"   Secret Key: {'*' * min(len(config.get('secret_access_key', '')), 20) if config.get('secret_access_key') else 'Not configured'}")
        print(f"   Project: {config.get('project', 'Not configured')}")
        print(f"   Endpoint: {config.get('endpoint', 'Not configured')}")
        print(f"\n📁 Config file: {CONFIG_FILE}")
        sys.exit(0)

    # Validate required arguments
    if not all([args.access_id, args.secret_key, args.project]):
        parser.print_help()
        print("\n❌ Error: --access-id, --secret-key, and --project are required", file=sys.stderr)
        sys.exit(1)

    # Setup AK credentials
    success = setup_ak(args.access_id, args.secret_key, args.project, args.endpoint)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
