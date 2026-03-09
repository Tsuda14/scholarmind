# ScholarMind 🦞

**Academic Research Automation Tool**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-❤-red.svg)](https://github.com/sponsors/YOUR_USERNAME)

Automate your academic research workflow with AI-powered paper search, download, and analysis.

---

## 🎯 Features

- **🔍 Multi-Source Search** - Search papers from Google Scholar, PubMed, and arXiv simultaneously
- **📥 Automatic Download** - Download PDFs from Sci-Hub, Unpaywall, and arXiv
- **🌐 Auto Translation** - Automatically translates Chinese queries to English for broader search
- **🧠 AI-Powered Analysis** - Extract key findings, methods, and data from papers
- **📊 Bilingual Reports** - Generate comprehensive reports in English and Chinese
- **🎯 Scenario-Based** - Optimized workflows for competitor research, literature review, and regulatory preparation
- **💻 CLI & Interactive** - Both command-line and interactive modes available

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Tsuda14/scholarmind.git
cd scholarmind

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ScholarMind
pip install -e .
```

### Basic Usage

```bash
# Interactive mode (recommended for beginners)
scholarmind interactive

# Command-line mode
scholarmind search "biocompatibility testing" --max-papers 10

# Advanced usage
scholarmind search "cardiac stent" \
  --scenario research \
  --max-papers 20 \
  --language both \
  --output report.md
```

---

## 📖 Documentation

- **[Installation Guide](INSTALL.md)** - Detailed installation instructions for CentOS 10
- **[Quick Start](QUICKSTART.md)** - Get started in 5 minutes
- **[Examples](EXAMPLES.md)** - Comprehensive usage examples
- **[Changelog](CHANGELOG.md)** - Version history and updates

---

## 💡 Use Cases

### Competitor Research
```bash
scholarmind search "medical device biocompatibility" \
  --scenario research \
  --max-papers 15 \
  --output competitor_analysis.md
```

### Literature Review
```bash
scholarmind search "tissue engineering scaffold" \
  --scenario review \
  --max-papers 30 \
  --output literature_review.md
```

### Regulatory Preparation
```bash
scholarmind search "FDA 510k medical device" \
  --scenario regulatory \
  --max-papers 10 \
  --output regulatory_report.md
```

---

## 🛠️ Configuration

### Configure AI Model (Optional)

```bash
# OpenAI
scholarmind config --model openai --api-key sk-your-key

# Claude
scholarmind config --model claude --api-key sk-your-key

# Local model (Ollama, etc.)
scholarmind config --model local --endpoint http://localhost:11434
```

### View Configuration

```bash
scholarmind config
```

---

## 📊 How It Works

```
User Input → Auto Translation → Multi-Source Search → PDF Download → AI Analysis → Report Generation
```

1. **Search**: Queries Google Scholar, PubMed, and arXiv
2. **Download**: Attempts to download PDFs from multiple sources
3. **Analyze**: Extracts metadata, key findings, and data
4. **Report**: Generates bilingual Markdown/HTML reports

---

## 🌟 Key Features Explained

### Auto Translation
Input Chinese keywords? ScholarMind automatically translates to English and searches both languages:
```bash
scholarmind search "生物相容性"
# Automatically searches both "生物相容性" and "biocompatibility"
```

### Scenario-Based Analysis
Different scenarios extract different information:
- **Research**: Clinical data, efficacy, safety metrics
- **Review**: Methods, conclusions, trends
- **Regulatory**: FDA/ISO standards, compliance requirements

### File Organization
All outputs are organized in `~/.scholarmind/`:
```
~/.scholarmind/
├── config.json          # User configuration
├── papers/              # Downloaded PDFs
└── reports/             # Generated reports
```

---

## ⚠️ Legal Disclaimer

**Important**: This tool uses Sci-Hub for PDF downloads, which may violate copyright laws in some jurisdictions. 

- ✅ Use for personal research and educational purposes only
- ✅ Prefer legal open access sources (Unpaywall, arXiv)
- ⚠️ Users are responsible for compliance with local laws
- ⚠️ Sci-Hub access may require VPN in some regions

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Google Scholar](https://scholar.google.com/)
- [PubMed/NCBI](https://pubmed.ncbi.nlm.nih.gov/)
- [arXiv](https://arxiv.org/)
- [Sci-Hub](https://sci-hub.se/)
- [Unpaywall](https://unpaywall.org/)
- All open science initiatives

---

## 💰 Support

If you find ScholarMind useful, consider supporting its development:

- ⭐ Star this repository
- 🐛 Report bugs and suggest features
- 💖 [Sponsor on GitHub](https://github.com/sponsors/Tsuda14)
- ☕ [Buy me a coffee](https://ko-fi.com/Tsuda14)

---

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/Tsuda14/scholarmind/issues)
- **Email**: tsudashou14@gmail.com

---

## 🗺️ Roadmap

### v1.1.0 (Planned)
- [ ] Web interface
- [ ] Batch processing
- [ ] Citation network analysis
- [ ] Figure/table extraction

### v1.2.0 (Future)
- [ ] Team collaboration features
- [ ] Cloud sync
- [ ] Mobile app
- [ ] Advanced visualization

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/Tsuda14/scholarmind?style=social)
![GitHub forks](https://img.shields.io/github/forks/Tsuda14/scholarmind?style=social)
![GitHub issues](https://img.shields.io/github/issues/Tsuda14/scholarmind)
![GitHub license](https://img.shields.io/github/license/Tsuda14/scholarmind)

---

**Made with ❤️ by [tsuda](https://github.com/Tsuda14)**

*Automating research, one paper at a time.*

---

## 🌐 中文文档

[中文版 README](README_CN.md) | [安装指南](INSTALL.md) | [快速开始](QUICKSTART.md)
