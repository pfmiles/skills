# ODPS 查询 Skill

一个轻量级、便携的 MaxCompute (ODPS) SQL 查询工具。

## 核心特性

- **零配置开箱即用**：脚本会自动管理 Python 虚拟环境和依赖，无需手动安装 `pyodps`。
- **全功能支持**：基于官方 SDK，完美支持 SQL 执行和 **Tunnel 数据下载**（无数据量限制）。
- **结果 CSV 输出**：标准 CSV 格式输出，方便与其他工具（如 Excel、Pandas）集成。
- **LogView 集成**：任务执行时会自动打印 LogView 链接，方便监控任务状态。

## 快速开始

### 1. 初始化配置

首次使用时，有两种方式配置您的 Access ID、Secret Key 和默认 Project：

#### 方式 A：交互式配置向导（推荐）

```bash
./run.sh configure.py
```

#### 方式 B：直接告诉 AI 助手配置

如果您在使用 Claude Code 等 AI 助手，可以直接提供您的凭证信息，AI 会自动帮您配置：

```bash
# AI 助手会自动执行类似以下命令：
./run.sh setup_ak.py --access-id YOUR_ACCESS_ID --secret-key YOUR_SECRET_KEY --project your_project_dev
```

**示例对话：**
```
用户：帮我配置 ODPS AK
      Access ID: LTAI5***
      Secret Key: abc123***
      Project: lzd_seller_platform_dev

AI：好的，我来帮您配置... [执行配置命令]
```

> **提示**：配置的 `Project` 必须是您有权限提交作业的**开发项目**（通常以 `_dev` 结尾，例如 `lzd_seller_platform_dev`），而不是生产数据源项目。

#### 查看当前配置

```bash
./run.sh setup_ak.py --show
```

### 2. 执行查询

直接运行 SQL 语句，结果将以 CSV 格式打印到屏幕。

```bash
./run.sh query.py --sql "SELECT * FROM your_table LIMIT 10"
```

## 高级用法

### 导出数据到文件

使用 `--output` 参数直接将结果保存为 CSV 文件（推荐）：

> **注意**：出于安全考虑，输出路径仅限当前目录或系统临时目录（如 `/tmp`）。

```bash
./run.sh query.py --sql "SELECT * FROM large_table" --output output.csv
```

或者使用 Shell 重定向：

### 临时切换项目

如果您需要在另一个项目中执行查询（且不想修改默认配置）：

```bash
./run.sh query.py --sql "..." --project other_project_dev
```

## 目录结构说明

```
.
├── run.sh                  # 统一执行入口（负责环境自举）
├── scripts/
│   ├── configure.py       # 交互式配置工具
│   ├── setup_ak.py        # 程序化 AK 配置工具（支持 AI 助手）
│   └── query.py           # 查询核心逻辑
├── SKILL.md               # AI 技能定义文件
├── README.md              # 英文说明文档
└── README-cn.md           # 中文说明文档
```

## 常见问题

**Q: 为什么提示 Access Denied?**
A: ODPS 要求 SQL 任务必须在有 `CreateInstance` 权限的项目中运行。请检查您配置的 Project 是否为开发项目。

**Q: 第一次运行为什么比较慢？**
A: 第一次运行时，脚本会自动创建 Python 虚拟环境并下载 `pyodps` 库。后续运行将是秒级的。

**Q: 支持哪些 SQL 语法？**
A: 支持所有 MaxCompute SQL 语法，脚本会将 SQL 原样透传给 ODPS 服务端。
