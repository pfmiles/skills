# ODPS Account AK Configuration Guide

## Overview

This guide explains how to configure ODPS (MaxCompute) Account Access Keys for the odps-query tool. There are multiple methods available to suit different workflows.

## Configuration Methods

### Method 1: Interactive Configuration Wizard (Human Users)

The traditional interactive approach prompts you for each credential:

```bash
./run.sh configure.py
```

**When to use:**
- First-time manual setup
- When you prefer guided configuration
- When updating credentials interactively

### Method 2: Programmatic Configuration (AI Assistants)

The programmatic approach allows Claude Code and other AI assistants to configure credentials directly:

```bash
./run.sh setup_ak.py --access-id <ID> --secret-key <KEY> --project <PROJECT>
```

**When to use:**
- Working with AI assistants like Claude Code
- Scripted or automated setups
- Quick reconfiguration without prompts

**Example conversation with Claude Code:**

```
You: Please configure my ODPS credentials:
     Access ID: LTAI5tABC123XYZ
     Secret Key: abc123secret456
     Project: lzd_seller_platform_dev

Claude: I'll configure those credentials for you.
        [Executes: ./run.sh setup_ak.py --access-id "LTAI5tABC123XYZ" ...]
        ✅ Configuration saved successfully!
```

### Method 3: Environment Variables (CI/CD & Production)

Override configuration file with environment variables:

```bash
export ODPS_ACCESS_ID="your_access_id"
export ODPS_SECRET_ACCESS_KEY="your_secret_key"
export ODPS_PROJECT="your_project_dev"
export ODPS_ENDPOINT="http://your-endpoint.com/api"

./run.sh query.py --sql "SELECT * FROM table"
```

**When to use:**
- CI/CD pipelines
- Production environments
- Temporary credential override
- Security-sensitive environments

## Configuration Storage

### Location
Credentials are stored in: `~/.odps_config.json`

### Security
- File permissions: `600` (owner read/write only)
- JSON format for easy parsing
- Secret keys are masked when displayed

### Structure
```json
{
    "access_id": "LTAI5***",
    "secret_access_key": "abc123***",
    "project": "your_project_dev",
    "endpoint": "http://service-all.ali-sg-lazada.odps.aliyun-inc.com/api"
}
```

## Credential Priority

The system checks credentials in this order:

1. **Environment Variables** (highest priority)
   - `ODPS_ACCESS_ID`
   - `ODPS_SECRET_ACCESS_KEY`
   - `ODPS_PROJECT`
   - `ODPS_ENDPOINT`

2. **Configuration File**
   - `~/.odps_config.json`

3. **Command-line Arguments**
   - `--project` flag overrides configured project

4. **Default Endpoint** (lowest priority)
   - Default: Lazada Singapore endpoint

## Managing Configuration

### View Current Configuration

```bash
./run.sh setup_ak.py --show
```

Output:
```
📋 Current ODPS Configuration:
   Access ID: LTAI5***
   Secret Key: **************
   Project: lzd_seller_platform_dev
   Endpoint: http://service-all.ali-sg-lazada.odps.aliyun-inc.com/api

📁 Config file: /Users/username/.odps_config.json
```

### Update Configuration

Simply run the configuration command again with new values:

```bash
./run.sh setup_ak.py --access-id "NEW_ID" --secret-key "NEW_SECRET" --project "NEW_PROJECT"
```

### Remove Configuration

```bash
rm ~/.odps_config.json
```

## Configuration Requirements

### Access ID
- Format: Usually starts with `LTAI`
- Example: `LTAI5tABC123XYZ`

### Secret Access Key
- Alphanumeric string
- Keep secure and never commit to version control

### Project Name
- **Must be a development project** (ends with `_dev`)
- You must have `CreateInstance` permission
- Example: `lzd_seller_platform_dev`
- ❌ Invalid: `lzd_seller_platform` (production project)

### Endpoint (Optional)
- Default: Lazada Singapore endpoint
- Custom endpoints supported for different regions

## Common Issues

### Issue 1: Access Denied Error

**Symptom:**
```
Error: Missing ODPS configuration. Please run 'run.sh configure.py' first.
```

**Solutions:**
1. Configure credentials using one of the methods above
2. Ensure configuration file exists and is readable
3. Check environment variables if using that method

### Issue 2: Permission Denied on Tables

**Symptom:**
```
ODPS Error: Access Denied
```

**Solutions:**
1. Verify you're using a **development project** (ends with `_dev`)
2. Check you have `CreateInstance` permission on the project
3. Apply for table access at:
   ```
   https://guard.alibaba-inc.com/mark/mark.htm/#/table/permission?projectName=<PROJECT>&tableName=<TABLE>
   ```

### Issue 3: Invalid Project

**Symptom:**
```
Project not found or access denied
```

**Solutions:**
1. Confirm project name is correct
2. Ensure project ends with `_dev`
3. Verify you have access to the project
4. Check with your ODPS administrator

## Security Best Practices

1. **Never commit credentials** to version control
   - Add `~/.odps_config.json` to `.gitignore`
   - Use environment variables in CI/CD

2. **Protect configuration file**
   - File permissions are automatically set to 600
   - Keep backups secure

3. **Rotate credentials regularly**
   - Update Access Keys periodically
   - Revoke old keys after rotation

4. **Use development projects**
   - Never configure production projects
   - Development projects have appropriate safeguards

5. **Environment-specific credentials**
   - Use different credentials for different environments
   - Use environment variables for production

## For AI Assistants (Claude Code)

When a user asks to configure ODPS credentials:

1. **Extract credentials** from user message
2. **Validate** project name (should end with `_dev`)
3. **Execute configuration**:
   ```bash
   ./run.sh setup_ak.py --access-id "<ID>" --secret-key "<KEY>" --project "<PROJECT>"
   ```
4. **Confirm** successful configuration
5. **Suggest** a test query to verify setup

**Example workflow:**
```bash
# User provides: Access ID, Secret Key, Project
# Claude executes:
./run.sh setup_ak.py \
  --access-id "LTAI5tABC123XYZ" \
  --secret-key "abc123secret456" \
  --project "lzd_seller_platform_dev"

# Verify configuration:
./run.sh setup_ak.py --show

# Suggest test query:
./run.sh query.py --sql "SELECT * FROM information_schema.tables LIMIT 5"
```

## Command Reference

### setup_ak.py Options

```bash
./run.sh setup_ak.py [OPTIONS]

Options:
  --access-id ID       ODPS Access ID (required)
  --secret-key KEY     ODPS Secret Access Key (required)
  --project PROJECT    ODPS Project Name (required, must end with _dev)
  --endpoint URL       ODPS Endpoint URL (optional)
  --show              Display current configuration
  -h, --help          Show help message
```

### Examples

**Configure new credentials:**
```bash
./run.sh setup_ak.py \
  --access-id "LTAI5tABC123XYZ" \
  --secret-key "abc123secret456" \
  --project "lzd_seller_platform_dev"
```

**Configure with custom endpoint:**
```bash
./run.sh setup_ak.py \
  --access-id "LTAI5tABC123XYZ" \
  --secret-key "abc123secret456" \
  --project "lzd_seller_platform_dev" \
  --endpoint "http://custom.endpoint.com/api"
```

**View configuration:**
```bash
./run.sh setup_ak.py --show
```

**Get help:**
```bash
./run.sh setup_ak.py --help
```

## Troubleshooting

### Debug Configuration Issues

1. **Check configuration exists:**
   ```bash
   ls -la ~/.odps_config.json
   ```

2. **View configuration:**
   ```bash
   ./run.sh setup_ak.py --show
   ```

3. **Check file permissions:**
   ```bash
   ls -l ~/.odps_config.json
   # Should show: -rw------- (600)
   ```

4. **Validate JSON format:**
   ```bash
   cat ~/.odps_config.json | python -m json.tool
   ```

5. **Test with environment variables:**
   ```bash
   export ODPS_ACCESS_ID="test"
   export ODPS_SECRET_ACCESS_KEY="test"
   export ODPS_PROJECT="test_dev"
   ./run.sh query.py --sql "SELECT 1"
   ```

## Support

For issues or questions:
- Check this guide first
- Review the main README.md
- Consult SKILL.md for AI assistant integration
- Contact your ODPS administrator for access issues
