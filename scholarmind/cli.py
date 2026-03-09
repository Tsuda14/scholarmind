#!/usr/bin/env python3
"""
CLI Interface for ScholarMind
命令行界面
"""

import click
import sys
from pathlib import Path
from .config import Config
from .search import search_papers
from .download import download_papers
from .analyze import analyze_papers
from .report import generate_report

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    ScholarMind - Academic Research Automation Tool
    学术研究自动化助手
    
    自动搜索、下载、分析学术论文并生成报告
    """
    pass

@cli.command()
@click.argument('query')
@click.option('--scenario', type=click.Choice(['research', 'review', 'regulatory', 'custom']), 
              default='custom', help='Research scenario / 研究场景')
@click.option('--max-papers', default=10, help='Maximum papers to download / 最大下载数量')
@click.option('--output', default='report.md', help='Output file / 输出文件')
@click.option('--language', default='both', type=click.Choice(['en', 'zh', 'both']), 
              help='Language preference / 语言偏好')
@click.option('--sources', default='all', help='Data sources (comma-separated) / 数据源')
def search(query, scenario, max_papers, output, language, sources):
    """
    Search and analyze papers / 搜索并分析论文
    
    Example:
        scholarmind search "biocompatibility testing"
        scholarmind search "心脏支架" --scenario research --max-papers 20
    """
    click.echo(f"🦞 ScholarMind v1.0.0")
    click.echo(f"📝 Query: {query}")
    click.echo(f"🎯 Scenario: {scenario}")
    click.echo(f"📚 Max papers: {max_papers}")
    click.echo()
    
    # Create output directory
    from pathlib import Path
    output_dir = Path.home() / '.scholarmind' / 'reports'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # If output is just filename, put it in reports directory
    output_path = Path(output)
    if not output_path.is_absolute() and output_path.parent == Path('.'):
        output = str(output_dir / output)
    
    # Step 1: Search
    click.echo("🔍 Step 1/4: Searching papers...")
    papers = search_papers(query, max_papers, sources)
    click.echo(f"   Found {len(papers)} papers")
    
    # Step 2: Download
    click.echo("📥 Step 2/4: Downloading papers...")
    downloaded = download_papers(papers, language)
    click.echo(f"   Downloaded {len(downloaded)} papers")
    
    # Step 3: Analyze
    click.echo("🧠 Step 3/4: Analyzing papers...")
    analysis = analyze_papers(downloaded, scenario)
    click.echo(f"   Analysis complete")
    
    # Step 4: Generate report
    click.echo("📊 Step 4/4: Generating report...")
    generate_report(analysis, output, language)
    click.echo(f"   ✅ Report saved to: {output}")
    click.echo()
    click.echo("🎉 Done! Enjoy your research! / 完成！祝研究顺利！")

@cli.command()
def interactive():
    """
    Interactive mode / 交互模式
    """
    click.echo("🦞 ScholarMind Interactive Mode")
    click.echo("=" * 50)
    click.echo()
    
    # Scenario selection
    click.echo("📋 Select research scenario / 选择研究场景:")
    click.echo("  1. Competitor Research / 竞品调研")
    click.echo("  2. Literature Review / 文献综述")
    click.echo("  3. Regulatory Preparation / 监管准备")
    click.echo("  4. Custom / 自定义")
    
    scenario_map = {
        '1': 'research',
        '2': 'review',
        '3': 'regulatory',
        '4': 'custom'
    }
    
    choice = click.prompt("Enter choice / 输入选择", type=str, default='4')
    scenario = scenario_map.get(choice, 'custom')
    
    # Query
    query = click.prompt("Enter search query / 输入搜索关键词", type=str)
    
    # Max papers
    max_papers = click.prompt("Max papers to download / 最大下载数量", type=int, default=10)
    
    # Language
    click.echo()
    click.echo("🌐 Language preference / 语言偏好:")
    click.echo("  1. English only / 仅英文")
    click.echo("  2. Chinese only / 仅中文")
    click.echo("  3. Both / 双语")
    
    lang_map = {'1': 'en', '2': 'zh', '3': 'both'}
    lang_choice = click.prompt("Enter choice / 输入选择", type=str, default='3')
    language = lang_map.get(lang_choice, 'both')
    
    # Output
    output = click.prompt("Output filename / 输出文件名", type=str, default='report.md')
    
    # Confirm
    click.echo()
    click.echo("=" * 50)
    click.echo(f"Query: {query}")
    click.echo(f"Scenario: {scenario}")
    click.echo(f"Max papers: {max_papers}")
    click.echo(f"Language: {language}")
    click.echo(f"Output: {output}")
    click.echo("=" * 50)
    
    if click.confirm("Start research? / 开始研究？"):
        # Run search
        ctx = click.get_current_context()
        ctx.invoke(search, query=query, scenario=scenario, max_papers=max_papers, 
                  output=output, language=language, sources='all')

@cli.command()
@click.option('--model', help='AI model provider (openai/claude/local)')
@click.option('--api-key', help='API key')
@click.option('--endpoint', help='API endpoint (for local models)')
def config(model, api_key, endpoint):
    """
    Configure AI model / 配置 AI 模型
    """
    cfg = Config()
    
    if model:
        cfg.set('model.provider', model)
        click.echo(f"✅ Model provider set to: {model}")
    
    if api_key:
        cfg.set('model.api_key', api_key)
        click.echo(f"✅ API key configured")
    
    if endpoint:
        cfg.set('model.endpoint', endpoint)
        click.echo(f"✅ Endpoint set to: {endpoint}")
    
    if not any([model, api_key, endpoint]):
        # Show current config
        click.echo("Current configuration / 当前配置:")
        click.echo(f"  Model: {cfg.get('model.provider', 'not set')}")
        click.echo(f"  Endpoint: {cfg.get('model.endpoint', 'not set')}")
        click.echo(f"  API Key: {'configured' if cfg.get('model.api_key') else 'not set'}")

def main():
    """Main entry point"""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\n\n👋 Interrupted by user / 用户中断")
        sys.exit(0)
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
