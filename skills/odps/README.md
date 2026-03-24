# ODPS Query Skill

A lightweight, portable MaxCompute (ODPS) SQL client.

## Features

- **Zero Configuration**: Automatically manages Python environment and dependencies.
- **Portable**: No hardcoded paths; works anywhere.
- **Powerful**: Supports ODPS Tunnel for unlimited result retrieval.

## Getting Started

1.  **Configure Credentials**

    There are two ways to configure your Access ID, Secret Key, and Project:

    **Option A: Interactive Configuration Wizard (Recommended)**

    ```bash
    ./run.sh configure.py
    ```

    **Option B: Direct Configuration via AI Assistant**

    If you're using Claude Code or similar AI assistants, you can directly provide your credentials and the AI will configure them for you:

    ```bash
    # AI will execute a command like:
    ./run.sh setup_ak.py --access-id YOUR_ACCESS_ID --secret-key YOUR_SECRET_KEY --project your_project_dev
    ```

    **Example conversation:**
    ```
    User: Please configure ODPS AK for me
          Access ID: LTAI5***
          Secret Key: abc123***
          Project: lzd_seller_platform_dev

    AI: I'll configure that for you... [executes configuration]
    ```

    **View Current Configuration:**
    ```bash
    ./run.sh setup_ak.py --show
    ```

2.  **Run Queries**

    Execute SQL directly:

    ```bash
    ./run.sh query.py --sql "SELECT * FROM your_table LIMIT 10"
    ```

## Usage Tips

*   **Export to File**:
    Use the `--output` parameter to save results directly to a CSV file.
    > **Note**: For security, output paths are restricted to the current directory and system temp folders (e.g., `/tmp`).
    ```bash
    ./run.sh query.py --sql "SELECT * FROM large_table" --output output.csv
    ```

*   **Switch Project**:
    ```bash
    ./run.sh query.py --sql "..." --project other_dev_project
    ```

## Directory Structure

```
.
├── run.sh                  # Universal entry point
├── scripts/
│   ├── configure.py       # Interactive configuration wizard
│   ├── setup_ak.py        # Programmatic AK configuration (AI assistant support)
│   └── query.py           # Query execution logic
├── SKILL.md               # AI skill definition
├── README.md              # English documentation
└── README-cn.md           # Chinese documentation
```
