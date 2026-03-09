"""
Report generation module
报告生成模块
"""

from typing import Dict
from datetime import datetime
from pathlib import Path

def generate_report(analysis: Dict, output_file: str, language: str = 'both'):
    """
    Generate research report
    生成研究报告
    
    Args:
        analysis: Analysis results
        output_file: Output filename
        language: Report language ('en', 'zh', 'both')
    """
    output_path = Path(output_file)
    
    if output_path.suffix == '.md':
        content = generate_markdown_report(analysis, language)
    elif output_path.suffix == '.html':
        content = generate_html_report(analysis, language)
    else:
        # Default to markdown
        content = generate_markdown_report(analysis, language)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_markdown_report(analysis: Dict, language: str) -> str:
    """
    Generate Markdown report
    生成 Markdown 报告
    """
    report = []
    
    # Header
    if language in ['both', 'en']:
        report.append("# Research Report")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Scenario:** {analysis['scenario']}")
        report.append("")
    
    if language in ['both', 'zh']:
        report.append("# 研究报告")
        report.append(f"**生成时间：** {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}")
        report.append(f"**研究场景：** {get_scenario_name_zh(analysis['scenario'])}")
        report.append("")
    
    # Summary
    summary = analysis.get('summary', {})
    
    if language in ['both', 'en']:
        report.append("## Summary")
        report.append(f"- **Total Papers:** {summary.get('total_papers', 0)}")
        report.append(f"- **Successfully Analyzed:** {summary.get('successfully_analyzed', 0)}")
        report.append(f"- **Year Range:** {summary.get('year_range', 'Unknown')}")
        report.append("")
        
        report.append("### Sources")
        for source, count in summary.get('main_sources', []):
            report.append(f"- {source}: {count} papers")
        report.append("")
    
    if language in ['both', 'zh']:
        report.append("## 摘要")
        report.append(f"- **论文总数：** {summary.get('total_papers', 0)}")
        report.append(f"- **成功分析：** {summary.get('successfully_analyzed', 0)}")
        report.append(f"- **年份范围：** {summary.get('year_range', '未知')}")
        report.append("")
        
        report.append("### 数据来源")
        for source, count in summary.get('main_sources', []):
            report.append(f"- {source}：{count} 篇")
        report.append("")
    
    # Individual papers
    if language in ['both', 'en']:
        report.append("## Papers")
        report.append("")
    
    if language in ['both', 'zh']:
        report.append("## 论文列表")
        report.append("")
    
    for i, paper in enumerate(analysis.get('papers', []), 1):
        report.append(f"### {i}. {paper['title']}")
        report.append("")
        
        # Metadata
        if language in ['both', 'en']:
            report.append(f"**Authors:** {', '.join(paper.get('authors', [])[:3])}")
            report.append(f"**Year:** {paper.get('year', 'Unknown')}")
            report.append(f"**Source:** {paper.get('source', 'Unknown')}")
            if paper.get('url'):
                report.append(f"**URL:** {paper['url']}")
            report.append("")
        
        if language in ['both', 'zh']:
            report.append(f"**作者：** {', '.join(paper.get('authors', [])[:3])}")
            report.append(f"**年份：** {paper.get('year', '未知')}")
            report.append(f"**来源：** {paper.get('source', '未知')}")
            if paper.get('url'):
                report.append(f"**链接：** {paper['url']}")
            report.append("")
        
        # Key findings
        if paper.get('key_findings'):
            if language in ['both', 'en']:
                report.append("**Key Findings:**")
                for finding in paper['key_findings'][:3]:
                    report.append(f"- {finding}")
                report.append("")
            
            if language in ['both', 'zh']:
                report.append("**关键发现：**")
                for finding in paper['key_findings'][:3]:
                    report.append(f"- {finding}")
                report.append("")
        
        # Data
        if paper.get('data'):
            if language in ['both', 'en']:
                report.append("**Data:**")
                for key, value in paper['data'].items():
                    report.append(f"- {key}: {value}")
                report.append("")
            
            if language in ['both', 'zh']:
                report.append("**数据：**")
                for key, value in paper['data'].items():
                    report.append(f"- {key}: {value}")
                report.append("")
        
        report.append("---")
        report.append("")
    
    # Footer
    if language in ['both', 'en']:
        report.append("## Notes")
        report.append("- This report was automatically generated by ScholarMind")
        report.append("- For research purposes only")
        report.append("")
    
    if language in ['both', 'zh']:
        report.append("## 说明")
        report.append("- 本报告由 ScholarMind 自动生成")
        report.append("- 仅供研究使用")
        report.append("")
    
    report.append("---")
    report.append("*Generated by ScholarMind 🦞 | 由 ScholarMind 生成 🦞*")
    
    return '\n'.join(report)

def generate_html_report(analysis: Dict, language: str) -> str:
    """
    Generate HTML report
    生成 HTML 报告
    """
    # Convert markdown to HTML (simple version)
    md_content = generate_markdown_report(analysis, language)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Research Report | 研究报告</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 5px; }}
        h3 {{ color: #7f8c8d; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        .footer {{ margin-top: 50px; text-align: center; color: #95a5a6; }}
    </style>
</head>
<body>
<pre>{md_content}</pre>
<div class="footer">
    <p>Generated by ScholarMind 🦞</p>
</div>
</body>
</html>"""
    
    return html

def get_scenario_name_zh(scenario: str) -> str:
    """Get Chinese name for scenario"""
    names = {
        'research': '竞品调研',
        'review': '文献综述',
        'regulatory': '监管准备',
        'custom': '自定义'
    }
    return names.get(scenario, '未知')
