"""
Paper download module
论文下载模块
"""

import requests
import time
from pathlib import Path
from typing import List, Dict
import hashlib

def download_papers(papers: List[Dict], language: str = 'both') -> List[Dict]:
    """
    Download papers from various sources
    从各种来源下载论文
    
    Args:
        papers: List of paper metadata
        language: Language preference ('en', 'zh', 'both')
    
    Returns:
        List of papers with download info
    """
    download_dir = Path.home() / '.scholarmind' / 'papers'
    download_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded = []
    
    for i, paper in enumerate(papers, 1):
        print(f"   [{i}/{len(papers)}] {paper.get('title', 'Unknown')[:50]}...")
        
        # Try to download
        pdf_path = download_paper(paper, download_dir)
        
        if pdf_path:
            paper['pdf_path'] = str(pdf_path)
            paper['downloaded'] = True
            downloaded.append(paper)
            print(f"      ✅ Downloaded")
        else:
            paper['downloaded'] = False
            print(f"      ⚠️  Failed to download")
            # Still include for metadata analysis
            downloaded.append(paper)
        
        time.sleep(2)  # Rate limiting
    
    return downloaded

def download_paper(paper: Dict, download_dir: Path) -> Path:
    """
    Download a single paper
    下载单篇论文
    
    Priority:
    1. Direct PDF link (arXiv, etc.)
    2. Sci-Hub (via DOI)
    3. Unpaywall (legal open access)
    """
    # Generate filename
    title_hash = hashlib.md5(paper['title'].encode()).hexdigest()[:8]
    filename = f"{title_hash}_{paper.get('year', 'unknown')}.pdf"
    pdf_path = download_dir / filename
    
    # Skip if already downloaded
    if pdf_path.exists():
        return pdf_path
    
    # Try arXiv direct download
    if paper.get('source') == 'arXiv' and paper.get('arxiv_id'):
        url = f"https://arxiv.org/pdf/{paper['arxiv_id']}.pdf"
        if download_from_url(url, pdf_path):
            return pdf_path
    
    # Try Sci-Hub
    if paper.get('doi'):
        if download_from_scihub(paper['doi'], pdf_path):
            return pdf_path
    
    # Try Unpaywall (legal open access)
    if paper.get('doi'):
        if download_from_unpaywall(paper['doi'], pdf_path):
            return pdf_path
    
    return None

def download_from_url(url: str, save_path: Path, timeout: int = 30) -> bool:
    """Download PDF from direct URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, stream=True)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
    
    except Exception as e:
        pass
    
    return False

def download_from_scihub(doi: str, save_path: Path) -> bool:
    """
    Download from Sci-Hub
    从 Sci-Hub 下载
    
    ⚠️  Legal disclaimer: Sci-Hub may violate copyright in some jurisdictions.
    Use for personal research only.
    """
    mirrors = [
        "https://sci-hub.se",
        "https://sci-hub.st",
        "https://sci-hub.ru",
        "https://sci-hub.wf",
        "https://sci-hub.ren"
    ]
    
    for mirror in mirrors:
        try:
            # Method 1: Direct DOI link
            url = f"{mirror}/{doi}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            
            # Get the page with longer timeout
            response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
            
            if response.status_code == 200:
                # Try multiple methods to find PDF
                
                # Method A: Look for direct PDF in response
                if response.headers.get('content-type', '').startswith('application/pdf'):
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    return True
                
                # Method B: Parse HTML for PDF link
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for iframe with PDF
                iframe = soup.find('iframe', {'id': 'pdf'})
                if iframe and iframe.get('src'):
                    pdf_url = iframe['src']
                    if not pdf_url.startswith('http'):
                        pdf_url = mirror + pdf_url
                    if download_from_url(pdf_url, save_path, timeout=60):
                        return True
                
                # Look for embed tag
                embed = soup.find('embed', {'type': 'application/pdf'})
                if embed and embed.get('src'):
                    pdf_url = embed['src']
                    if not pdf_url.startswith('http'):
                        pdf_url = mirror + pdf_url
                    if download_from_url(pdf_url, save_path, timeout=60):
                        return True
                
                # Look for direct PDF links
                import re
                pdf_links = re.findall(r'(https?://[^\s"\'<>]+\.pdf[^\s"\'<>]*)', response.text)
                for pdf_link in pdf_links:
                    if download_from_url(pdf_link, save_path, timeout=60):
                        return True
                
                # Method C: Look for download button
                download_button = soup.find('button', {'onclick': re.compile(r'location\.href')})
                if download_button:
                    onclick = download_button.get('onclick', '')
                    pdf_match = re.search(r'location\.href\s*=\s*["\']([^"\']+)["\']', onclick)
                    if pdf_match:
                        pdf_url = pdf_match.group(1)
                        if not pdf_url.startswith('http'):
                            pdf_url = mirror + pdf_url
                        if download_from_url(pdf_url, save_path, timeout=60):
                            return True
        
        except Exception as e:
            continue
    
    return False

def download_from_unpaywall(doi: str, save_path: Path) -> bool:
    """
    Download from Unpaywall (legal open access)
    从 Unpaywall 下载（合法开放获取）
    """
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email=research@example.com"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check for open access PDF
            if data.get('is_oa'):
                pdf_url = data.get('best_oa_location', {}).get('url_for_pdf')
                
                if pdf_url:
                    if download_from_url(pdf_url, save_path):
                        return True
    
    except Exception:
        pass
    
    return False
