# ScholarMind v1.0.1 更新说明 🦞

**更新时间：** 2026-03-09 08:20 MDT

---

## 🎉 新功能

### 1. 增强的 PDF 下载功能 📥

**问题：** 之前即使有代理也无法下载 PDF

**解决方案：**
- ✅ 增加了更多 Sci-Hub 镜像（5个）
- ✅ 改进了 PDF 提取算法（支持多种方法）
- ✅ 增加了超时时间（30秒 → 60秒）
- ✅ 支持多种 PDF 链接格式（iframe、embed、direct link）
- ✅ 更好的 HTML 解析（BeautifulSoup）

**新的 Sci-Hub 镜像：**
- https://sci-hub.se
- https://sci-hub.st
- https://sci-hub.ru
- https://sci-hub.wf
- https://sci-hub.ren

### 2. 中文自动翻译 🌐

**问题：** 输入中文只搜索中文论文

**解决方案：**
- ✅ 自动检测中文输入
- ✅ 自动翻译成英文
- ✅ 同时搜索中英文关键词
- ✅ 使用 Google Translate API（免费）

**示例：**
```bash
# 输入中文
scholarmind search "生物相容性"

# 自动翻译并搜索
🌐 Detected Chinese query, translating...
📝 English query: biocompatibility
# 同时搜索 "生物相容性" 和 "biocompatibility"
```

### 3. 文件管理优化 📁

**问题：** 报告文件平铺在根目录，混乱

**解决方案：**
- ✅ 自动创建 `~/.scholarmind/reports/` 文件夹
- ✅ 所有报告默认保存到该文件夹
- ✅ PDF 文件保存到 `~/.scholarmind/papers/`
- ✅ 配置文件在 `~/.scholarmind/config.json`

**文件结构：**
```
~/.scholarmind/
├── config.json          # 配置文件
├── papers/              # 下载的 PDF
│   ├── abc123_2024.pdf
│   └── def456_2025.pdf
└── reports/             # 生成的报告
    ├── report.md
    ├── 生物相容性研究.md
    └── cardiac_stent.md
```

---

## 🔧 技术改进

### PDF 下载算法

**之前：**
```python
# 简单的正则匹配
pdf_match = re.search(r'(https?://[^"]+\.pdf[^"]*)', response.text)
```

**现在：**
```python
# 多种方法尝试
1. 检查 Content-Type 是否为 PDF
2. 查找 <iframe id="pdf"> 标签
3. 查找 <embed type="application/pdf"> 标签
4. 正则匹配所有 PDF 链接
5. 查找下载按钮的 onclick 事件
```

### 翻译功能

**使用 Google Translate API：**
- 免费、无需 API key
- 支持中文 → 英文
- 自动检测中文字符
- 翻译失败时使用原查询

---

## 📊 测试结果

### 中文翻译测试
```bash
scholarmind search "生物相容性" --max-papers 3 --sources "pubmed"
```

**结果：**
- ✅ 自动检测中文
- ✅ 翻译成 "biocompatibility"
- ✅ 找到 1 篇论文
- ✅ 报告保存到 `~/.scholarmind/reports/report.md`

### 文件管理测试
```bash
ls ~/.scholarmind/
# 输出：
# config.json  papers/  reports/
```

---

## 🚀 使用示例

### 中文搜索（自动翻译）
```bash
scholarmind search "心脏支架" --max-papers 20
# 自动翻译成 "cardiac stent" 并同时搜索
```

### 指定输出文件
```bash
scholarmind search "biocompatibility" --output 我的研究.md
# 保存到：~/.scholarmind/reports/我的研究.md
```

### 查看所有报告
```bash
ls ~/.scholarmind/reports/
```

### 查看下载的 PDF
```bash
ls ~/.scholarmind/papers/
```

---

## ⚠️ 注意事项

### PDF 下载

虽然改进了下载算法，但仍可能失败，原因：
1. Sci-Hub 镜像被封锁
2. 论文没有 DOI
3. 论文不在 Sci-Hub 数据库中
4. 网络问题

**建议：**
- 使用日本/美国等地区的代理
- 优先使用 arXiv（合法且稳定）
- 手动下载后放到 `~/.scholarmind/papers/`

### 翻译功能

- 仅支持中文 → 英文
- 翻译质量依赖 Google Translate
- 翻译失败时使用原查询（不影响使用）

---

## 🔮 未来计划

### v1.0.2
- [ ] 支持更多翻译方向（英 → 中）
- [ ] 改进 PDF 解析（OCR 支持）
- [ ] 添加进度条
- [ ] 支持断点续传

### v1.1.0
- [ ] Web 界面
- [ ] 批量处理
- [ ] 引用网络分析
- [ ] 图表提取

---

## 📝 更新日志

### v1.0.1 (2026-03-09)
- ✅ 增强 PDF 下载（5个镜像 + 多种提取方法）
- ✅ 中文自动翻译
- ✅ 文件管理优化（reports/ 文件夹）
- ✅ 修复 arXiv 解析 bug

### v1.0.0 (2026-03-09)
- ✅ 初始版本
- ✅ 基础搜索功能
- ✅ PDF 下载
- ✅ 双语报告生成

---

**更新完成！现在可以更好地使用 ScholarMind 了！** 🦞🎉

*如有问题，随时反馈！*
