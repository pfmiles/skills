---
name: odps
version: 0.2.0
description: MaxCompute (ODPS) data query skill. Includes an automated SQL agent for complex analysis. Supports SQL execution with automatic result downloading via Tunnel.
---

# ODPS Query Skill

A portable, self-bootstrapping tool for querying MaxCompute (ODPS) data.

## Capabilities

### 1. Execute SQL

Executes SQL statements and retrieves results as CSV.

**Usage:**
```bash
./run.sh query.py --sql "<SQL_STATEMENT>"
```

**Parameters:**
*   `--sql`: (Required) The SQL statement to execute.
*   `--output`: (Optional) Path to save results as CSV (e.g., `/tmp/result.csv`). **Security Note**: Path must be within the skill's directory or the system temporary directory (e.g., `/tmp`).
*   `--project`: (Optional) Override the default project name.

**Example:**
```bash
./run.sh query.py --sql "SELECT * FROM sales LIMIT 100" --output /tmp/sales_data.csv
```

### 2. Configuration

**Interactive Configuration:**
```bash
./run.sh configure.py
```

**Programmatic Configuration (For AI Assistants):**

When users provide Account AK credentials directly in conversation, use this command to configure them automatically:

```bash
./run.sh setup_ak.py --access-id <ACCESS_ID> --secret-key <SECRET_KEY> --project <PROJECT_NAME> [--endpoint <ENDPOINT_URL>]
```

**Parameters:**
*   `--access-id`: ODPS Access ID (required)
*   `--secret-key`: ODPS Secret Access Key (required)
*   `--project`: ODPS Project Name - must be a development project (required)
*   `--endpoint`: ODPS Endpoint URL (optional, defaults to Lazada Singapore endpoint)
*   `--show`: Display current configuration without making changes

**Example Usage Scenario:**

When a user says:
```
User: Please configure my ODPS credentials
      Access ID: LTAI5tABC123XYZ
      Secret Key: abc123secret456
      Project: lzd_seller_platform_dev
```

Claude should execute:
```bash
./run.sh setup_ak.py --access-id "LTAI5tABC123XYZ" --secret-key "abc123secret456" --project "lzd_seller_platform_dev"
```

**Configuration Guidelines:**
1. **Validate Project Name**: Ensure project ends with `_dev` (development project)
2. **Security**: Credentials are saved to `~/.odps_config.json` with secure permissions (600)
3. **Confirmation**: Always confirm successful configuration and suggest a test query
4. **View Config**: Use `--show` flag to display current configuration (secrets are masked)

## Specialized Agents

### ODPS SQL Executor
Located at: `agents/odps-sql-executor.md`

Use this agent to execute ODPS SQL queries, especially when parallel execution is beneficial.

**Capabilities:**
*   Executes ODPS SQL queries.
*   **Parallel Execution**: Can run multiple queries simultaneously.
*   Returns raw results for further processing.

**Best Practice:**
When facing multiple queries or time-consuming operations, rationally plan to delegate these tasks to the `odps-sql-executor` subagent to ensure efficiency.

## Reference Documentation

For detailed SQL generation guidelines (syntax mapping, performance tips, etc.), please refer to:

**`reference/ODPS_SQL_PROMPT_GUIDE.md`**

When generating SQL, Claude should consult this guide to ensure ODPS compliance.

## Important Notes

*   **Self-Contained**: The skill manages its own Python venv.
*   **Relative Paths**: Execute scripts relative to the skill root.
*   **Permissions**: Ensure your configured project has `CreateInstance` permission (use `_dev` projects).
*   **Tunneling**: Large result sets are automatically downloaded via ODPS Tunnel.
*   **Permission Handling**: If a permission issue occurs (e.g., Access Denied), generate a permission application URL: `https://guard.alibaba-inc.com/mark/mark.htm/#/table/permission?projectName=<PROJECT_NAME>&tableName=<TABLE_NAME>` and instruct the user to apply.
*   **Cost & Requirement Clarity**: ODPS queries are paid services. **Do not execute queries based on ambiguous requirements.** Always clarify the user's intent, request DDL if schema is missing, and preview data (`LIMIT n`) when necessary.
*   **Partition Safety**: For all partitioned tables (especially those using `ds` or `pt`), **ALWAYS** restrict the query to the latest partition by default using `ds = MAX_PT('table_name')` or `pt = MAX_PT('table_name')`, unless the user explicitly specifies a partition range. Refer to `reference/ODPS_SQL_PROMPT_GUIDE.md` for details.
*   **Default Trust**: Do not proactively check for configuration or credentials. Assume the environment is correctly configured. Only verify or request Access Key (AK) configuration if an operation specifically fails due to missing credentials (e.g., `odps.errors.ODPSError`).
*   **Execution Strategy**: Prioritize using the sub-agent (`agents/odps-sql-executor.md`) for SQL tasks to leverage parallel execution.
    *   If the sub-agent is found in `agents/`, use it.
    *   If NOT found/installed, **urgently prompt the user to install it**.
    *   Fallback to direct `query.py` execution only if the sub-agent is unavailable or the task is trivial.
*   **Reporting**: After a successful query, generate a Markdown report (e.g., `report.md`) in the execution directory. This report must include:
    *   The **Executed SQL Statement**.
    *   The **Path to the Resulting CSV File**.

## Handling Configuration Issues

When users encounter Account AK configuration issues:

1. **Missing Configuration**: If query fails with missing credentials, guide user to configure:
   - Option 1: Interactive wizard: `./run.sh configure.py`
   - Option 2: Tell Claude credentials directly (Claude will use `setup_ak.py`)

2. **Invalid Credentials**: If access denied, check:
   - Project must be development project (ends with `_dev`)
   - User has `CreateInstance` permission on the project
   - Generate permission URL: `https://guard.alibaba-inc.com/mark/mark.htm/#/table/permission?projectName=<PROJECT>&tableName=<TABLE>`

3. **View Configuration**: To diagnose issues, check current config:
   ```bash
   ./run.sh setup_ak.py --show
   ```

## Files

*   `run.sh`: Entry point wrapper.
*   `scripts/query.py`: Main query logic.
*   `scripts/configure.py`: Interactive configuration wizard.
*   `scripts/setup_ak.py`: Programmatic AK configuration (for AI assistants).
*   `agents/odps-sql-executor.md`: Parallel execution agent.
*   `reference/ODPS_SQL_PROMPT_GUIDE.md`: SQL best practices.
