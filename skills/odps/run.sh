#!/bin/bash
set -e

# Skill 根目录
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="$BASE_DIR/.venv"
PIP_INDEX="https://mirrors.aliyun.com/pypi/simple/"

# 1. 检查并初始化 Python 环境
if [ ! -d "$VENV_DIR" ]; then
    echo "⚙️  Initializing Python environment for the first time..."
    
    # 检查 python3 是否存在
    if ! command -v python3 &> /dev/null; then
        echo "❌ Error: python3 is required but not found."
        exit 1
    fi
    
    # 创建虚拟环境
    python3 -m venv "$VENV_DIR"
    
    # 安装依赖
    echo "📦 Installing dependencies (pyodps)..."
    "$VENV_DIR/bin/pip" install -q pyodps -i "$PIP_INDEX"
    
    echo "✅ Environment ready."
fi

# 2. 参数处理
SCRIPT_NAME="$1"
shift # 移除第一个参数

# 自动补全脚本路径
TARGET_SCRIPT=""
if [ -f "$BASE_DIR/scripts/$SCRIPT_NAME" ]; then
    TARGET_SCRIPT="$BASE_DIR/scripts/$SCRIPT_NAME"
elif [ -f "$BASE_DIR/$SCRIPT_NAME" ]; then
    TARGET_SCRIPT="$BASE_DIR/$SCRIPT_NAME"
else
    echo "❌ Script not found: $SCRIPT_NAME"
    echo "Usage: $0 <script_name> [args...]"
    exit 1
fi

# 3. 运行脚本
exec "$VENV_DIR/bin/python" "$TARGET_SCRIPT" "$@"
