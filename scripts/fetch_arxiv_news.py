#!/usr/bin/env python3
"""
arXiv AI News Fetcher for AI News Hub
自动获取最新 AI 研究论文并格式化为 Markdown
"""

import requests
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any
import xml.etree.ElementTree as ET
import sys
from dateutil import parser

class ArxivNewsFetcher:
    """Fetch and format AI research news from arXiv"""

    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query"
        self.categories = ['cs.AI', 'cs.LG', 'cs.CL', 'cs.RO']

    def fetch_recent_papers(self, days: int = 7, max_results: int = 15) -> List[Dict[str, Any]]:
        """
        Fetch recent papers from arXiv using API

        Args:
            days: Number of days to look back (default: 7, extended to catch slower submission periods)
            max_results: Maximum number of papers to return

        Returns:
            List of paper dictionaries
        """
        # Calculate date range
        date_threshold = datetime.utcnow() - timedelta(days=days)

        # Search for AI-related papers
        search_query = (
            f"cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.RO"
        )

        params = {
            'search_query': search_query,
            'start': 0,
            'max_results': max_results * 2,  # Fetch more to filter
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()

            # Parse XML response
            root = ET.fromstring(response.content)

            # Define namespace
            ns = {
                'atom': 'http://www.w3.org/2005/Atom',
                'arxiv': 'http://arxiv.org/schemas/atom'
            }

            papers = []
            for entry in root.findall('atom:entry', ns):
                # Extract paper info
                paper_id = entry.find('atom:id', ns).text.split('/')[-1]

                # Parse published date
                from dateutil import parser
                published_str = entry.find('atom:published', ns).text
                published = parser.parse(published_str)

                # Filter by date (use naive comparison, ignore timezone)
                if published.tzinfo:
                    published = published.replace(tzinfo=None)

                if published < date_threshold:
                    continue

                # Extract title
                title = entry.find('atom:title', ns).text.strip()

                # Extract authors
                authors = []
                for author in entry.findall('atom:author', ns):
                    name = author.find('atom:name', ns).text
                    authors.append(name)

                # Extract summary
                summary = entry.find('atom:summary', ns).text.strip()
                summary = re.sub(r'\s+', ' ', summary)  # Clean whitespace

                # Extract categories
                categories = []
                for cat in entry.findall('atom:category', ns):
                    cat_term = cat.get('term')
                    if cat_term:
                        categories.append(cat_term)

                # Extract primary category
                primary_category = entry.find('arxiv:primary_category', ns)
                if primary_category is not None:
                    primary_cat = primary_category.get('term')
                else:
                    primary_cat = categories[0] if categories else 'cs.AI'

                # Build paper dict
                paper = {
                    'id': paper_id,
                    'title': title,
                    'authors': authors[:5],  # Limit to first 5 authors
                    'abstract': summary[:500] + '...' if len(summary) > 500 else summary,
                    'published': published_str,
                    'categories': categories,
                    'primary_category': primary_cat,
                    'url': f"https://arxiv.org/abs/{paper_id}",
                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf"
                }

                papers.append(paper)

                if len(papers) >= max_results:
                    break

            return papers

        except Exception as e:
            print(f"Error fetching arXiv papers: {e}", file=sys.stderr)
            return []

    def format_as_markdown(self, papers: List[Dict[str, Any]]) -> str:
        """Format papers as Markdown"""

        today = datetime.now().strftime('%Y-%m-%d')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        md_content = f"""# {today} AI News 每日简报

**日期**: {timestamp}
**来源**: arXiv CS.AI + cs.LG
**覆盖范围**: 过去48小时
**语言**: 中英文混合 🌐

---

## 📰 今日要闻

共收集 {len(papers)} 条最新 AI 研究

---

"""

        # Format each paper
        for i, paper in enumerate(papers, 1):
            # Format published date for display
            pub_dt = parser.parse(paper['published'])
            pub_display = pub_dt.strftime('%Y-%m-%d %H:%M')

            md_content += f"""### {paper['title']}

**来源**: arXiv {paper['primary_category'].upper()}
**时间**: {pub_display}
**链接**: [{paper['id']}]({paper['url']})

**摘要**: {paper['abstract']}

**作者**: {', '.join(paper['authors'])}
**分类**: {', '.join(paper['categories'])}

---

"""

        # Add footer
        md_content += f"""
---
**更新时间**: {timestamp}
**数据来源**: arXiv.org
**由**: 贾维斯 (JARVIS) 自动生成 🤖
"""

        return md_content

    def save_to_file(self, content: str, filepath: str) -> bool:
        """Save markdown content to file"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 新闻已保存到: {filepath}", file=sys.stderr)
            return True
        except Exception as e:
            print(f"❌ 保存文件失败: {e}", file=sys.stderr)
            return False


def main():
    """Main function"""
    import os

    # Initialize fetcher
    fetcher = ArxivNewsFetcher()

    # Fetch recent papers
    print("📡 正在获取 arXiv 最新论文...", file=sys.stderr)
    papers = fetcher.fetch_recent_papers(days=7, max_results=15)

    if not papers:
        print("❌ 未能获取到任何论文", file=sys.stderr)
        sys.exit(1)

    print(f"✅ 获取到 {len(papers)} 篇论文", file=sys.stderr)

    # Format as markdown
    print("📝 正在格式化为 Markdown...", file=sys.stderr)
    md_content = fetcher.format_as_markdown(papers)

    # Generate filename
    today = datetime.now().strftime('%Y-%m-%d')
    output_dir = "/data1/cc/vide-coding/ai-news-hub/docs/news"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/{today}.md"

    # Save to file
    if fetcher.save_to_file(md_content, output_file):
        print(f"✅ 成功生成新闻文件: {output_file}", file=sys.stderr)
        print(output_file)  # Print filename for cron to capture
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
