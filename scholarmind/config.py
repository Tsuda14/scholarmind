"""
Configuration management
配置管理
"""

import json
from pathlib import Path
import os

class Config:
    """Configuration manager"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.scholarmind'
        self.config_file = self.config_dir / 'config.json'
        self.config_dir.mkdir(exist_ok=True)
        self.load()
    
    def load(self):
        """Load configuration"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.data = json.load(f)
        else:
            self.data = self.default_config()
            self.save()
    
    def save(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get(self, key, default=None):
        """Get config value by dot notation"""
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def set(self, key, value):
        """Set config value by dot notation"""
        keys = key.split('.')
        data = self.data
        for k in keys[:-1]:
            if k not in data:
                data[k] = {}
            data = data[k]
        data[keys[-1]] = value
        self.save()
    
    def default_config(self):
        """Default configuration"""
        return {
            "model": {
                "provider": "openai",
                "api_key": "",
                "endpoint": ""
            },
            "search": {
                "default_max_papers": 10,
                "sources": ["pubmed", "scholar", "arxiv"]
            },
            "download": {
                "scihub_mirrors": [
                    "https://sci-hub.se",
                    "https://sci-hub.st",
                    "https://sci-hub.ru"
                ],
                "timeout": 30,
                "retry": 3
            },
            "language": {
                "default": "both",
                "translate": True
            }
        }
