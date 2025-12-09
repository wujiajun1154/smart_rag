# SmartRAG · 轻量级检索增强对话系统

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-06B6D4?logo=langchain)](https://python.langchain.com)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-00A67E?logo=openai)](https://platform.openai.com)

**中文 | [English](./README_EN.md)**

SmartRAG 是一套**本地RAG**（Retrieval-Augmented Generation）流水线：
- 自动抓取与问题最相关的 **3 条网页**
- 基于 **BAAI/bge-small-zh-v1.5** 构建向量索引
- 支持 **多轮上下文记忆** 的 DeepSeek-r1 对话
- 全程 **命令行交互**！

---

## 🌟 核心特性

| 功能    | 状态 | 备注 |
|-------| --- | --- |
| 网页搜索  | ✅ | Tavily API Top-3 |
| 中英文嵌入 | ✅ | BAAI/bge-small-zh-v1.5 |
| 向量检索  | ✅ | Chroma + 可调 top-k |
| 多轮记忆  | ✅ | ConversationBufferMemory |
| Web UI | 🚧 | Roadmap |

---

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/YOUR_NAME/SmartRAG.git
cd SmartRAG
```
### 2. 创建虚拟环境（推荐）
#### 使用 conda（推荐）
```bash
conda create -n smartrag python=3.10 -y
conda activate smartrag
```
##### 或使用 venv
```bash
python -m venv venv
```
#### Windows
```bash
venv\Scripts\activate
```
#### macOS/Linux
```bash
source venv/bin/activate
```
### 3.安装依赖
```bash
pip install -r requirements.txt
```

### 编辑 .env 文件，填写以下字段：
```bash
TAVILY_API_KEY=tvly-xxx                          # Tavily 搜索 API
OPENAI_API_KEY=sk-xxx                            # OpenAI 或代理站密钥
OPENAI_BASE_URL=https://api.openai.com/v1        # 国内可换代理，例如 https://api.132ai.com/v1
```
###4. 配置密钥
### 5. 运行对话
```bash
python -m my_rag.cli_demo
```
## 项目结构
<pre>
SmartRAG/
├── my_rag/
│   ├── cli.py              # 命令行入口
│   ├── web_catch.py        # Tavily 搜索 + WebBaseLoader 解析
│   ├── embedding.py        # 文档分块、BAAI 嵌入、Chroma 建库
│   ├── core_chain.py       # ConversationalRetrievalChain 带记忆链
│   └── utils/
│       └── env_utils.py    # 读取环境变量
├── tests/
│   └── test_core_chain.py  # 核心链单元测试
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
</pre>