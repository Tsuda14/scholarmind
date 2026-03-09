"""
Paper analysis module
论文分析模块
"""

import PyPDF2
from typing import List, Dict
import os

def analyze_papers(papers: List[Dict], scenario: str = 'custom') -> Dict:
    """
    Analyze downloaded papers
    分析下载的论文
    
    Args:
        papers: List of papers with PDF paths
        scenario: Research scenario
    
    Returns:
        Analysis results
    """
    analysis = {
        'scenario': scenario,
        'total_papers': len(papers),
        'downloaded_papers': sum(1 for p in papers if p.get('downloaded')),
        'papers': []
    }
    
    for paper in papers:
        paper_analysis = analyze_single_paper(paper, scenario)
        analysis['papers'].append(paper_analysis)
    
    # Generate summary
    analysis['summary'] = generate_summary(analysis, scenario)
    
    return analysis

def analyze_single_paper(paper: Dict, scenario: str) -> Dict:
    """
    Analyze a single paper
    分析单篇论文
    """
    result = {
        'title': paper.get('title', ''),
        'authors': paper.get('authors', []),
        'year': paper.get('year', ''),
        'source': paper.get('source', ''),
        'url': paper.get('url', ''),
        'downloaded': paper.get('downloaded', False)
    }
    
    # Extract text from PDF if available
    if paper.get('pdf_path') and os.path.exists(paper['pdf_path']):
        text = extract_text_from_pdf(paper['pdf_path'])
        result['text_extracted'] = True
        result['text_length'] = len(text)
        
        # Basic analysis
        result['key_findings'] = extract_key_findings(text, scenario)
        result['methods'] = extract_methods(text)
        result['data'] = extract_data(text, scenario)
    else:
        result['text_extracted'] = False
        result['abstract'] = paper.get('abstract', '')
    
    return result

def extract_text_from_pdf(pdf_path: str, max_pages: int = 50) -> str:
    """
    Extract text from PDF
    从 PDF 提取文本
    """
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            
            for i, page in enumerate(reader.pages):
                if i >= max_pages:
                    break
                text += page.extract_text() + '\n'
            
            return text
    
    except Exception as e:
        return ''

def extract_key_findings(text: str, scenario: str) -> List[str]:
    """
    Extract key findings from text
    提取关键发现
    
    Simple keyword-based extraction
    (In production, use AI model here)
    """
    findings = []
    
    # Keywords based on scenario
    if scenario == 'research':
        keywords = ['efficacy', 'safety', 'performance', 'outcome', 'result']
    elif scenario == 'regulatory':
        keywords = ['FDA', 'approval', 'clearance', '510(k)', 'compliance', 'standard']
    else:
        keywords = ['conclusion', 'result', 'finding', 'significant']
    
    # Simple extraction (split by sentences and find keywords)
    sentences = text.split('.')
    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(kw in sentence_lower for kw in keywords):
            findings.append(sentence.strip())
            if len(findings) >= 5:
                break
    
    return findings

def extract_methods(text: str) -> str:
    """
    Extract research methods
    提取研究方法
    """
    # Look for Methods/Materials section
    methods_keywords = ['methods', 'materials', 'methodology', 'experimental']
    
    text_lower = text.lower()
    for keyword in methods_keywords:
        idx = text_lower.find(keyword)
        if idx != -1:
            # Extract ~500 chars after keyword
            return text[idx:idx+500].strip()
    
    return "Methods section not found"

def extract_data(text: str, scenario: str) -> Dict:
    """
    Extract specific data based on scenario
    根据场景提取特定数据
    """
    data = {}
    
    if scenario == 'research':
        # Extract sample size, p-values, etc.
        import re
        
        # Sample size
        n_match = re.search(r'n\s*=\s*(\d+)', text, re.IGNORECASE)
        if n_match:
            data['sample_size'] = n_match.group(1)
        
        # P-values
        p_matches = re.findall(r'p\s*[<>=]\s*0\.\d+', text, re.IGNORECASE)
        if p_matches:
            data['p_values'] = p_matches[:5]
    
    elif scenario == 'regulatory':
        # Extract regulatory info
        if 'FDA' in text:
            data['fda_mentioned'] = True
        if '510(k)' in text:
            data['510k_mentioned'] = True
        if 'ISO' in text:
            data['iso_mentioned'] = True
    
    return data

def generate_summary(analysis: Dict, scenario: str) -> Dict:
    """
    Generate overall summary
    生成总体摘要
    """
    summary = {
        'total_papers': analysis['total_papers'],
        'successfully_analyzed': sum(1 for p in analysis['papers'] if p.get('text_extracted')),
        'year_range': get_year_range(analysis['papers']),
        'main_sources': get_main_sources(analysis['papers'])
    }
    
    return summary

def get_year_range(papers: List[Dict]) -> str:
    """Get year range of papers"""
    years = [int(p['year']) for p in papers if p.get('year') and p['year'].isdigit()]
    if years:
        return f"{min(years)}-{max(years)}"
    return "Unknown"

def get_main_sources(papers: List[Dict]) -> List[str]:
    """Get main sources"""
    sources = {}
    for paper in papers:
        source = paper.get('source', 'Unknown')
        sources[source] = sources.get(source, 0) + 1
    
    return sorted(sources.items(), key=lambda x: x[1], reverse=True)
