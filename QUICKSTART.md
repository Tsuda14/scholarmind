# 🚀 ScholarMind 快速开始指南

**5 分钟上手 ScholarMind！**

---

## 第一步：激活环境

```bash
cd /home/tsuda/.openclaw/workspace/scholarmind
source venv/bin/activate
```

你会看到命令行前面出现 `(venv)`

---

## 第二步：验证安装

```bash
scholarmind --version
```

应该输出：`scholarmind, version 1.0.0`

---

## 第三步：开始使用

### 方式 1：交互模式（推荐新手）

```bash
scholarmind interactive
```

然后按提示操作：
1. 选择场景（1-4）
2. 输入关键词
3. 设置论文数量
4. 选择语言
5. 输入文件名
6. 确认开始

### 方式 2：命令行模式（快速）

```bash
# 基础搜索
scholarmind search "你的关键词" --max-papers 10

# 医疗器械研究
scholarmind search "biocompatibility testing" \
  --scenario research \
  --max-papers 15 \
  --output 生物相容性研究.md

# 文献综述
scholarmind search "cardiac stent" \
  --scenario review \
  --max-papers 30 \
  --language both \
  --output 心脏支架综述.md
```

---

## 第四步：查看报告

```bash
# 查看生成的报告
cat 生物相容性研究.md

# 或用编辑器打开
nano 生物相容性研究.md
```

---

## 常用命令速查

```bash
# 查看帮助
scholarmind --help
scholarmind search --help

# 配置 AI 模型（可选）
scholarmind config --model openai --api-key sk-xxx

# 查看当前配置
scholarmind config

# 指定数据源
scholarmind search "query" --sources "pubmed,arxiv"

# 生成 HTML 报告
scholarmind search "query" --output report.html
```

---

## 场景说明

| 场景 | 适用于 | 提取内容 |
|------|--------|----------|
| `research` | 竞品调研 | 临床数据、安全性、有效性 |
| `review` | 文献综述 | 研究方法、结论、趋势 |
| `regulatory` | 监管准备 | FDA、ISO 标准、合规性 |
| `custom` | 自定义 | 通用分析 |

---

## 示例：完整工作流

```bash
# 1. 激活环境
cd /home/tsuda/.openclaw/workspace/scholarmind
source venv/bin/activate

# 2. 搜索论文
scholarmind search "medical device biocompatibility ISO 10993" \
  --scenario regulatory \
  --max-papers 20 \
  --language both \
  --output ISO10993研究.md

# 3. 查看报告
cat ISO10993研究.md

# 4. 如果需要更多论文，再次搜索
scholarmind search "biocompatibility testing methods" \
  --max-papers 15 \
  --output 测试方法.md

# 5. 完成后退出环境
deactivate
```

---

## 故障排除

### 问题：找不到 scholarmind 命令

**解决：**
```bash
# 确保激活了虚拟环境
source /home/tsuda/.openclaw/workspace/scholarmind/venv/bin/activate

# 或重新安装
cd /home/tsuda/.openclaw/workspace/scholarmind
pip install -e .
```

### 问题：下载失败

**原因：** Sci-Hub 可能被封锁

**解决：**
1. 使用 VPN
2. 或只使用 PubMed/arXiv：`--sources "pubmed,arxiv"`
3. 或手动下载 PDF 后放到 `~/.scholarmind/papers/`

### 问题：搜索很慢

**解决：**
1. 减少论文数量：`--max-papers 5`
2. 指定单一数据源：`--sources "pubmed"`
3. 避免高峰时段

---

## 下次使用

```bash
# 每次使用前激活环境
cd /home/tsuda/.openclaw/workspace/scholarmind
source venv/bin/activate

# 使用完毕后退出
deactivate
```

---

## 进阶技巧

### 批量处理

```bash
# 创建关键词列表
cat > keywords.txt << EOF
biocompatibility
sterilization
clinical trial
EOF

# 批量搜索
while read keyword; do
  scholarmind search "$keyword" --max-papers 10 --output "${keyword}.md"
done < keywords.txt
```

### 定时任务

```bash
# 每天自动搜索最新论文
crontab -e

# 添加：
0 9 * * * cd ~/scholarmind && source venv/bin/activate && scholarmind search "medical device" --max-papers 5 --output ~/reports/daily_$(date +\%Y\%m\%d).md
```

---

**准备好了吗？开始你的研究之旅！** 🦞🚀

*有问题随时问我！*
