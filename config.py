"""
配置文件
"""

# 监控的URL列表
URLS = [
    {
        'name': 'trending-games',
        'url': 'https://azgames.io/trending-games',
        'display_name': '热门趋势游戏'
    },
    {
        'name': 'hot-games',
        'url': 'https://azgames.io/hot-games',
        'display_name': '火爆游戏'
    },
    {
        'name': 'popular-games',
        'url': 'https://azgames.io/popular-games',
        'display_name': '流行游戏'
    }
]

# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 数据文件路径
DATA_FILE = 'games_data.json'
