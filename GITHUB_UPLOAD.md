# 上传到 GitHub 指南 🦞

## 步骤 1: 初始化 Git 仓库

```bash
cd /home/tsuda/.openclaw/workspace/scholarmind

# 初始化 Git
git init

# 添加所有文件
git add .

# 第一次提交
git commit -m "Initial commit: ScholarMind v1.0.1 - Academic Research Automation Tool"
```

## 步骤 2: 在 GitHub 创建仓库

1. 去 https://github.com
2. 点击右上角 "+" → "New repository"
3. 填写信息：
   - **Repository name**: `scholarmind`
   - **Description**: `Academic Research Automation Tool - AI-powered paper search, download, and analysis | 学术研究自动化助手`
   - **Public** (开源) 或 **Private** (私有)
   - ❌ 不要勾选 "Initialize with README" (我们已经有了)
4. 点击 "Create repository"

## 步骤 3: 连接并推送

GitHub 会显示命令，复制执行：

```bash
# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/scholarmind.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 步骤 4: 设置 GitHub Sponsors（可选）

1. 去你的 GitHub 个人设置
2. 找到 "Sponsors" 或 "GitHub Sponsors"
3. 设置收款方式（Stripe/PayPal）
4. 在仓库添加 "Sponsor" 按钮

## 步骤 5: 添加 Topics 标签

在 GitHub 仓库页面：
1. 点击 "About" 旁边的齿轮图标
2. 添加 Topics:
   - `academic-research`
   - `paper-search`
   - `pdf-download`
   - `ai-tools`
   - `python`
   - `cli-tool`
   - `research-automation`
   - `scholarly`

## 步骤 6: 推广

### Reddit
- r/academia
- r/scholar
- r/GradSchool
- r/Python

### Twitter/X
```
🦞 Introducing ScholarMind - Academic Research Automation Tool

✅ Auto search papers (Google Scholar, PubMed, arXiv)
✅ Auto download PDFs
✅ AI-powered analysis
✅ Bilingual reports (EN/ZH)

Open source & free!
https://github.com/YOUR_USERNAME/scholarmind

#AcademicTwitter #OpenScience #Python
```

### 知乎
发布文章：《我做了一个学术研究自动化工具》

### Product Hunt
提交产品（需要准备截图和演示）

---

## 文件检查清单

在上传前确认这些文件都在：

- [x] README.md - 主文档
- [x] LICENSE - MIT 协议
- [x] requirements.txt - 依赖
- [x] setup.py - 安装配置
- [x] .gitignore - Git 忽略文件
- [x] INSTALL.md - 安装指南
- [x] EXAMPLES.md - 使用示例
- [x] CHANGELOG.md - 更新日志
- [x] QUICKSTART.md - 快速开始
- [x] scholarmind/ - 源代码

---

## 注意事项

### ⚠️ 不要上传的文件：
- ❌ venv/ (虚拟环境)
- ❌ __pycache__/ (Python 缓存)
- ❌ *.pyc (编译文件)
- ❌ 测试生成的报告
- ❌ API keys

### ✅ 应该上传的：
- ✅ 所有源代码
- ✅ 文档
- ✅ LICENSE
- ✅ requirements.txt
- ✅ setup.py

---

## 快速命令

```bash
# 一键上传（替换 YOUR_USERNAME）
cd /home/tsuda/.openclaw/workspace/scholarmind
git init
git add .
git commit -m "Initial commit: ScholarMind v1.0.1"
git remote add origin https://github.com/YOUR_USERNAME/scholarmind.git
git branch -M main
git push -u origin main
```

---

## 后续更新

每次更新后：

```bash
git add .
git commit -m "Update: 描述你的更改"
git push
```

---

**准备好了吗？开始上传吧！** 🦞🚀
