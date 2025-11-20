"""
游戏爬虫模块
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from config import HEADERS


def fetch_games(url: str) -> List[Dict[str, str]]:
    """
    从指定URL抓取游戏列表
    
    Args:
        url: 目标网页URL
        
    Returns:
        游戏列表，每个游戏包含name和url
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=30, verify=True)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        games = []
        
        # 查找所有游戏链接
        game_links = soup.find_all('a', href=True)
        
        # 过滤页脚和分类链接
        excluded_paths = [
            '/category/', '/about-us', '/copyright-infringement',
            '/contact-us', '/privacy-policy', '/term-of-use'
        ]
        
        for link in game_links:
            href = link.get('href', '')
            
            # 转换相对路径为绝对路径
            if href.startswith('/'):
                href = 'https://azgames.io' + href
            
            # 只保留游戏链接
            if (href.startswith('https://azgames.io/') and 
                not any(ex in href for ex in excluded_paths) and
                href != 'https://azgames.io/' and
                href != 'https://azgames.io'):
                
                game_name = link.get_text(strip=True)
                # 移除标签
                game_name = game_name.replace('Trending', '').replace('Updated', '').strip()
                
                if game_name and href and len(game_name) > 0:
                    games.append({
                        'name': game_name,
                        'url': href
                    })
        
        # 去重
        seen_urls = set()
        unique_games = []
        for game in games:
            if game['url'] not in seen_urls:
                seen_urls.add(game['url'])
                unique_games.append(game)
        
        return unique_games
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求失败 {url}: {e}")
        return []
    except Exception as e:
        print(f"❌ 解析失败 {url}: {e}")
        import traceback
        traceback.print_exc()
        return []
