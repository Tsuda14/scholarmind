# ScholarMind Usage Examples | 使用示例

## Example 1: Quick Search | 快速搜索

```bash
scholarmind search "biocompatibility testing"
```

**Output:**
- Searches Google Scholar, PubMed, arXiv
- Downloads up to 10 papers
- Generates `report.md` with bilingual summary

---

## Example 2: Interactive Mode | 交互模式

```bash
scholarmind interactive
```

**Interactive prompts:**
1. Select scenario (竞品调研/文献综述/监管准备/自定义)
2. Enter search query
3. Set max papers
4. Choose language preference
5. Specify output filename

---

## Example 3: Competitor Research | 竞品调研

```bash
scholarmind search "cardiac stent biocompatibility" \
  --scenario research \
  --max-papers 20 \
  --language both \
  --output cardiac_stent_research.md
```

**What it does:**
- Focuses on clinical data, safety, efficacy
- Extracts sample sizes, p-values
- Compares different products
- Generates bilingual report

---

## Example 4: Literature Review | 文献综述

```bash
scholarmind search "medical device sterilization methods" \
  --scenario review \
  --max-papers 30 \
  --sources "pubmed,scholar" \
  --output sterilization_review.md
```

**What it does:**
- Comprehensive literature search
- Extracts methods and conclusions
- Organizes by year and source
- Suitable for systematic reviews

---

## Example 5: Regulatory Preparation | 监管准备

```bash
scholarmind search "FDA 510k Class II medical device" \
  --scenario regulatory \
  --max-papers 15 \
  --output regulatory_analysis.md
```

**What it does:**
- Focuses on FDA, ISO standards
- Extracts regulatory requirements
- Identifies predicate devices
- Helps with 510(k) preparation

---

## Example 6: Chinese Medical Device Research | 中文医疗器械研究

```bash
scholarmind search "心脏支架 生物相容性" \
  --scenario research \
  --max-papers 25 \
  --language both \
  --output 心脏支架研究.md
```

**What it does:**
- Searches both English and Chinese papers
- Translates key findings
- Generates bilingual report
- Suitable for Chinese market research

---

## Example 7: Custom Sources | 自定义数据源

```bash
scholarmind search "tissue engineering scaffold" \
  --sources "pubmed,arxiv" \
  --max-papers 15 \
  --output tissue_engineering.md
```

**What it does:**
- Only searches specified sources
- Useful when you know where to look
- Faster than searching all sources

---

## Example 8: HTML Report | HTML 报告

```bash
scholarmind search "implantable medical devices" \
  --max-papers 10 \
  --output report.html
```

**What it does:**
- Generates HTML report instead of Markdown
- Better for presentations
- Includes styling and formatting

---

## Configuration Examples | 配置示例

### Configure OpenAI

```bash
scholarmind config --model openai --api-key sk-your-openai-key
```

### Configure Claude

```bash
scholarmind config --model claude --api-key sk-your-claude-key
```

### Configure Local Model (Ollama)

```bash
# First, start Ollama server
ollama serve

# Then configure ScholarMind
scholarmind config --model local --endpoint http://localhost:11434
```

### View Current Configuration

```bash
scholarmind config
```

**Output:**
```
Current configuration / 当前配置:
  Model: openai
  Endpoint: https://api.openai.com/v1
  API Key: configured
```

---

## Advanced Usage | 高级用法

### Batch Processing | 批量处理

```bash
# Create a list of queries
cat > queries.txt << EOF
biocompatibility testing
sterilization methods
clinical trial design
EOF

# Process each query
while read query; do
  scholarmind search "$query" --max-papers 10 --output "${query// /_}.md"
done < queries.txt
```

### Automated Daily Research | 自动化每日研究

```bash
# Add to crontab
crontab -e

# Run daily at 9 AM
0 9 * * * cd ~/scholarmind && source venv/bin/activate && scholarmind search "medical device news" --max-papers 5 --output ~/reports/daily_$(date +\%Y\%m\%d).md
```

### Integration with Other Tools | 与其他工具集成

```bash
# Export to JSON for further processing
scholarmind search "query" --output report.md

# Convert to PDF
pandoc report.md -o report.pdf

# Send via email
mail -s "Research Report" user@example.com < report.md
```

---

## Tips & Tricks | 技巧

### 1. Use Specific Keywords | 使用具体关键词

❌ Bad: "medical device"
✅ Good: "cardiac stent biocompatibility ISO 10993"

### 2. Combine English and Chinese | 结合中英文

```bash
scholarmind search "心脏支架 cardiac stent" --language both
```

### 3. Start Small, Then Scale | 从小开始，逐步扩大

```bash
# First, test with 5 papers
scholarmind search "query" --max-papers 5

# If results are good, scale up
scholarmind search "query" --max-papers 50
```

### 4. Use Scenarios | 使用场景模式

Different scenarios extract different information:
- `research`: Clinical data, efficacy, safety
- `review`: Methods, conclusions, trends
- `regulatory`: Standards, approvals, compliance

### 5. Check Downloaded Papers | 检查下载的论文

```bash
# Papers are stored in:
ls ~/.scholarmind/papers/

# View a paper
evince ~/.scholarmind/papers/abc123_2024.pdf
```

---

## Troubleshooting Examples | 故障排除示例

### No Papers Downloaded

```bash
# Check internet connection
ping google.com

# Try different sources
scholarmind search "query" --sources "arxiv"  # arXiv is usually accessible

# Check Sci-Hub status
curl -I https://sci-hub.se
```

### Slow Performance

```bash
# Reduce max papers
scholarmind search "query" --max-papers 5

# Use specific sources
scholarmind search "query" --sources "pubmed"
```

### API Rate Limiting

```bash
# Add delays between requests (edit config)
nano ~/.scholarmind/config.json

# Increase delay:
"download": {
  "delay_seconds": 5  # Increase from default 2
}
```

---

**Happy researching! | 祝研究顺利！** 🦞
