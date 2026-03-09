# Installation Guide for CentOS 10 | CentOS 10 安装指南

## Prerequisites | 前置要求

### System Requirements | 系统要求
- CentOS 10 (or compatible RHEL-based system)
- Python 3.8 or higher
- 2GB RAM minimum
- Internet connection

### 系统要求
- CentOS 10（或兼容的 RHEL 系统）
- Python 3.8 或更高版本
- 最少 2GB 内存
- 互联网连接

---

## Step 1: Install Python 3 | 安装 Python 3

```bash
# Check Python version
python3 --version

# If Python 3.8+ is not installed:
sudo dnf install python3 python3-pip python3-devel

# Verify installation
python3 --version
pip3 --version
```

---

## Step 2: Install System Dependencies | 安装系统依赖

```bash
# Install required system packages
sudo dnf install -y gcc gcc-c++ make git

# Install development tools
sudo dnf groupinstall -y "Development Tools"
```

---

## Step 3: Clone Repository | 克隆仓库

```bash
# Clone ScholarMind
cd ~
git clone https://github.com/yourusername/scholarmind.git
cd scholarmind

# Or download and extract if no git
# wget https://github.com/yourusername/scholarmind/archive/main.zip
# unzip main.zip
# cd scholarmind-main
```

---

## Step 4: Create Virtual Environment | 创建虚拟环境

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
```

---

## Step 5: Install Python Dependencies | 安装 Python 依赖

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install ScholarMind
pip install -e .
```

---

## Step 6: Verify Installation | 验证安装

```bash
# Check if scholarmind is installed
scholarmind --version

# Should output: ScholarMind v1.0.0

# Run help
scholarmind --help
```

---

## Step 7: Configure AI Model | 配置 AI 模型

```bash
# Configure your AI model (choose one)

# Option 1: OpenAI
scholarmind config --model openai --api-key sk-your-key-here

# Option 2: Claude
scholarmind config --model claude --api-key sk-your-key-here

# Option 3: Local model (Ollama)
scholarmind config --model local --endpoint http://localhost:11434
```

---

## Step 8: Test Run | 测试运行

```bash
# Run a simple test
scholarmind search "test query" --max-papers 2

# If successful, you should see:
# 🦞 ScholarMind v1.0.0
# 📝 Query: test query
# ...
```

---

## Troubleshooting | 故障排除

### Problem: "command not found: scholarmind"

**Solution:**
```bash
# Make sure virtual environment is activated
source ~/scholarmind/venv/bin/activate

# Or add to PATH
export PATH="$HOME/scholarmind/venv/bin:$PATH"

# Add to ~/.bashrc for permanent
echo 'export PATH="$HOME/scholarmind/venv/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Problem: "ModuleNotFoundError"

**Solution:**
```bash
# Reinstall dependencies
cd ~/scholarmind
source venv/bin/activate
pip install -r requirements.txt --force-reinstall
```

### Problem: "Permission denied"

**Solution:**
```bash
# Don't use sudo with pip in virtual environment
# If you see permission errors, check:
ls -la ~/scholarmind/venv

# Fix ownership if needed
sudo chown -R $USER:$USER ~/scholarmind
```

### Problem: PDF download fails

**Solution:**
```bash
# Check internet connection
ping google.com

# Try different Sci-Hub mirrors (configured in config)
scholarmind config

# Use VPN if Sci-Hub is blocked in your region
```

---

## Firewall Configuration | 防火墙配置

If you need to access external APIs:

```bash
# Allow outbound HTTPS (usually already allowed)
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

---

## Uninstallation | 卸载

```bash
# Remove virtual environment
rm -rf ~/scholarmind/venv

# Remove ScholarMind directory
rm -rf ~/scholarmind

# Remove config
rm -rf ~/.scholarmind
```

---

## Performance Tips | 性能优化

### For faster downloads:
```bash
# Increase max concurrent downloads (edit config)
nano ~/.scholarmind/config.json

# Change:
"download": {
  "max_concurrent": 5  # Increase from default 3
}
```

### For large-scale research:
```bash
# Use SSD for paper storage
mkdir -p /path/to/fast/storage/papers
ln -s /path/to/fast/storage/papers ~/.scholarmind/papers
```

---

## Automatic Startup | 自动启动

To run ScholarMind as a service (optional):

```bash
# Create systemd service file
sudo nano /etc/systemd/system/scholarmind.service

# Add:
[Unit]
Description=ScholarMind Service
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/home/your-username/scholarmind
ExecStart=/home/your-username/scholarmind/venv/bin/python -m scholarmind.cli
Restart=on-failure

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable scholarmind
sudo systemctl start scholarmind
```

---

## Support | 支持

If you encounter issues:
1. Check logs: `~/.scholarmind/logs/`
2. GitHub Issues: https://github.com/Tsuda14/scholarmind/issues
3. Email: tsudashou14@gmail.com

---

**Installation complete! Happy researching! | 安装完成！祝研究顺利！** 🦞
