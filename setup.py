from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="scholarmind",
    version="1.0.0",
    author="tsuda",
    author_email="tsudashou14@gmail.com",
    description="Academic Research Automation Tool | 学术研究自动化助手",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tsuda14/scholarmind",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "requests>=2.28.0",
        "scholarly>=1.7.0",
        "PyPDF2>=3.0.0",
        "feedparser>=6.0.0",
        "beautifulsoup4>=4.11.0",
        "lxml>=4.9.0",
    ],
    entry_points={
        "console_scripts": [
            "scholarmind=scholarmind.cli:main",
        ],
    },
)
