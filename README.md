# ScholarMind 🦞

**Academic Research Automation Tool | 学术研究自动化助手**

Version 1.0.0

---

## 🎯 What is ScholarMind?

ScholarMind is a powerful command-line tool that automates academic research workflows:

1. **🔍 Smart Search** - AI-optimized keyword generation + multi-source search
2. **📥 Auto Download** - Download papers from Google Scholar, PubMed, arXiv, Sci-Hub
3. **🧠 AI Analysis** - Extract key findings, methods, and data
4. **📊 Report Generation** - Generate bilingual (EN/ZH) research reports

**ScholarMind 是什么？**

ScholarMind 是一个强大的命令行工具，可自动化学术研究流程：

1. **🔍 智能搜索** - AI 优化关键词 + 多源搜索
2. **📥 自动下载** - 从 Google Scholar、PubMed、arXiv、Sci-Hub 下载论文
3. **🧠 AI 分析** - 提取关键发现、方法和数据
4. **📊 报告生成** - 生成中英双语研究报告

---

## ✨ Features | 功能特性

- ✅ **Multi-source search** | 多源搜索 (Google Scholar, PubMed, arXiv)
- ✅ **Automatic download** | 自动下载 (Sci-Hub, Unpaywall)
- ✅ **PDF parsing** | PDF 解析
- ✅ **AI-powered analysis** | AI 驱动分析
- ✅ **Bilingual reports** | 双语报告 (EN/ZH)
- ✅ **Multiple scenarios** | 多场景支持 (竞品调研/文献综述/监管准备)
- ✅ **Interactive mode** | 交互模式
- ✅ **Configurable AI models** | 可配置 AI 模型

---

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Clone repository
git clone https://github.com/yourusername/scholarmind.git
cd scholarmind

# Install dependencies
pip install -r requirements.txt

# Install ScholarMind
pip install -e .
```

### Basic Usage | 基本使用

```bash
# Simple search
scholarmind search "biocompatibility testing"

# Interactive mode
scholarmind interactive

# Custom scenario
scholarmind search "心脏支架" --scenario research --max-papers 20 --output report.md
```

---

## 📖 Usage Examples | 使用示例

### Example 1: Competitor Research | 竞品调研

```bash
scholarmind search "medical device biocompatibility" \
  --scenario research \
  --max-papers 15 \
  --language both \
  --output competitor_analysis.md
```

### Example 2: Literature Review | 文献综述

```bash
scholarmind search "cardiac stent clinical trials" \
  --scenario review \
  --max-papers 30 \
  --output literature_review.md
```

### Example 3: Regulatory Preparation | 监管准备

```bash
scholarmind search "FDA 510k medical device" \
  --scenario regulatory \
  --max-papers 10 \
  --output regulatory_report.md
```

---

## 🛠️ Configuration | 配置

### Configure AI Model | 配置 AI 模型

```bash
# OpenAI
scholarmind config --model openai --api-key sk-xxx

# Claude
scholarmind config --model claude --api-key sk-xxx

# Local model (Ollama, etc.)
scholarmind config --model local --endpoint http://localhost:11434
```

### View Configuration | 查看配置

```bash
scholarmind config
```

---

## 📋 Command Reference | 命令参考

### `scholarmind search`

Search and analyze papers | 搜索并分析论文

**Options:**
- `--scenario` - Research scenario (research/review/regulatory/custom)
- `--max-papers` - Maximum papers to download (default: 10)
- `--output` - Output filename (default: report.md)
- `--language` - Language preference (en/zh/both, default: both)
- `--sources` - Data sources (comma-separated, default: all)

### `scholarmind interactive`

Interactive mode with guided prompts | 交互模式

### `scholarmind config`

Configure AI model and settings | 配置 AI 模型和设置

---

## 🗂️ Project Structure | 项目结构

```
scholarmind/
├── scholarmind/
│   ├── __init__.py
│   ├── cli.py          # Command-line interface
│   ├── search.py       # Paper search
│   ├── download.py     # Paper download
│   ├── analyze.py      # Paper analysis
│   ├── report.py       # Report generation
│   └── config.py       # Configuration
├── requirements.txt
├── setup.py
├── README.md
└── INSTALL.md
```

---

## ⚠️ Legal Disclaimer | 法律声明

**English:**
- Sci-Hub may violate copyright laws in some jurisdictions
- This tool is for personal research and educational purposes only
- Users are responsible for compliance with local laws
- Always prefer legal open access sources (Unpaywall, arXiv, etc.)

**中文：**
- Sci-Hub 在某些地区可能违反版权法
- 本工具仅供个人研究和教育用途
- 用户需自行遵守当地法律
- 请优先使用合法开放获取资源（Unpaywall、arXiv 等）

---

## 🤝 Contributing | 贡献

Contributions are welcome! | 欢迎贡献！

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📄 License | 许可证

MIT License

---

## 🙏 Acknowledgments | 致谢

- Google Scholar
- PubMed/NCBI
- arXiv
- Sci-Hub
- Unpaywall
- All open science initiatives

---

## 📞 Support | 支持

- **Issues:** [GitHub Issues](https://github.com/yourusername/scholarmind/issues)
- **Email:** support@example.com
- **Sponsor:** [GitHub Sponsors](https://github.com/sponsors/yourusername)

---

**Made with ❤️ by tsuda & 龙虾 🦞**

*Automating research, one paper at a time | 自动化研究，一次一篇论文*
