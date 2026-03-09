"""
Paper search module
论文搜索模块
"""

import requests
from scholarly import scholarly
import time
from typing import List, Dict
import re

def is_chinese(text: str) -> bool:
    """Check if text contains Chinese characters"""
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def translate_to_english(chinese_text: str) -> str:
    """
    Translate Chinese to English using free API
    使用免费 API 将中文翻译成英文
    """
    try:
        # Use Google Translate API (free, no key required)
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            'client': 'gtx',
            'sl': 'zh-CN',
            'tl': 'en',
            'dt': 't',
            'q': chinese_text
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            # Extract translated text
            translated = ''.join([item[0] for item in result[0] if item[0]])
            return translated
    except Exception as e:
        print(f"   ⚠️  Translation failed, using original query")
    
    return chinese_text

def search_papers(query: str, max_papers: int = 10, sources: str = 'all') -> List[Dict]:
    """
    Search papers from multiple sources
    从多个数据源搜索论文
    
    Args:
        query: Search query
        max_papers: Maximum number of papers
        sources: Data sources (comma-separated or 'all')
    
    Returns:
        List of paper metadata
    """
    papers = []
    
    # Auto-translate Chinese to English
    queries = [query]
    if is_chinese(query):
        print(f"   🌐 Detected Chinese query, translating...")
        english_query = translate_to_english(query)
        print(f"   📝 English query: {english_query}")
        queries.append(english_query)
    
    source_list = sources.split(',') if sources != 'all' else ['scholar', 'pubmed', 'arxiv']
    
    # Search with all queries
    for search_query in queries:
        for source in source_list:
            source = source.strip()
            if source == 'scholar':
                papers.extend(search_google_scholar(search_query, max_papers // (len(source_list) * len(queries))))
            elif source == 'pubmed':
                papers.extend(search_pubmed(search_query, max_papers // (len(source_list) * len(queries))))
            elif source == 'arxiv':
                papers.extend(search_arxiv(search_query, max_papers // (len(source_list) * len(queries))))
    
    # Remove duplicates by DOI/title
    seen = set()
    unique_papers = []
    for paper in papers:
        identifier = paper.get('doi') or paper.get('title', '').lower()
        if identifier and identifier not in seen:
            seen.add(identifier)
            unique_papers.append(paper)
    
    return unique_papers[:max_papers]

def search_google_scholar(query: str, max_results: int = 10) -> List[Dict]:
    """
    Search Google Scholar
    搜索 Google Scholar
    """
    papers = []
    
    try:
        search_query = scholarly.search_pubs(query)
        
        for i, result in enumerate(search_query):
            if i >= max_results:
                break
            
            paper = {
                'title': result.get('bib', {}).get('title', ''),
                'authors': result.get('bib', {}).get('author', []),
                'year': result.get('bib', {}).get('pub_year', ''),
                'abstract': result.get('bib', {}).get('abstract', ''),
                'url': result.get('pub_url', ''),
                'doi': extract_doi(result.get('pub_url', '')),
                'source': 'Google Scholar'
            }
            
            papers.append(paper)
            time.sleep(1)  # Rate limiting
    
    except Exception as e:
        print(f"   ⚠️  Google Scholar error: {e}")
    
    return papers

def search_pubmed(query: str, max_results: int = 10) -> List[Dict]:
    """
    Search PubMed
    搜索 PubMed
    """
    papers = []
    
    try:
        # PubMed E-utilities API (free, no key required for low volume)
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        
        # Search
        search_url = f"{base_url}esearch.fcgi"
        params = {
            'db': 'pubmed',
            'term': query,
            'retmax': max_results,
            'retmode': 'json'
        }
        
        response = requests.get(search_url, params=params, timeout=10)
        data = response.json()
        
        pmids = data.get('esearchresult', {}).get('idlist', [])
        
        if not pmids:
            return papers
        
        # Fetch details
        fetch_url = f"{base_url}esummary.fcgi"
        params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'json'
        }
        
        response = requests.get(fetch_url, params=params, timeout=10)
        data = response.json()
        
        for pmid in pmids:
            article = data.get('result', {}).get(pmid, {})
            
            paper = {
                'title': article.get('title', ''),
                'authors': [a.get('name', '') for a in article.get('authors', [])],
                'year': article.get('pubdate', '').split()[0] if article.get('pubdate') else '',
                'abstract': '',  # Need separate call for abstract
                'url': f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                'doi': article.get('elocationid', '').replace('doi: ', ''),
                'pmid': pmid,
                'source': 'PubMed'
            }
            
            papers.append(paper)
    
    except Exception as e:
        print(f"   ⚠️  PubMed error: {e}")
    
    return papers

def search_arxiv(query: str, max_results: int = 10) -> List[Dict]:
    """
    Search arXiv
    搜索 arXiv
    """
    papers = []
    
    try:
        import feedparser
        import urllib.parse
        
        # URL encode the query to handle spaces and special characters
        encoded_query = urllib.parse.quote(query)
        url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={max_results}"
        
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            try:
                paper = {
                    'title': entry.get('title', ''),
                    'authors': [author.name for author in entry.get('authors', [])],
                    'year': entry.get('published', '')[:4] if entry.get('published') else '',
                    'abstract': entry.get('summary', ''),
                    'url': entry.get('link', ''),
                    'doi': entry.get('arxiv_doi', ''),
                    'arxiv_id': entry.get('id', '').split('/abs/')[-1] if entry.get('id') else '',
                    'source': 'arXiv'
                }
                
                papers.append(paper)
            except Exception as e:
                continue
    
    except Exception as e:
        print(f"   ⚠️  arXiv error: {e}")
    
    return papers

def extract_doi(url: str) -> str:
    """Extract DOI from URL"""
    doi_pattern = r'10\.\d{4,}/[^\s]+'
    match = re.search(doi_pattern, url)
    return match.group(0) if match else ''
