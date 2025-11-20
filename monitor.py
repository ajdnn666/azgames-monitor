"""
监控主程序
"""
import json
import os
from datetime import datetime
from typing import Dict, List
from scraper import fetch_games
from config import URLS, DATA_FILE


def load_data() -> Dict:
    """加载历史数据"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}


def save_data(data: Dict):
    """保存数据"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def find_new_games(old_games: List[Dict], new_games: List[Dict]) -> List[Dict]:
    """查找新增游戏"""
    old_urls = {game['url'] for game in old_games}
    return [game for game in new_games if game['url'] not in old_urls]


def create_issue_body(results: List[Dict]) -> str:
    """创建 GitHub Issue 内容"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    body = f"## 🎮 新游戏检测报告\n\n"
    body += f"**检测时间**: {timestamp}\n\n"
    
    total_new = sum(len(r['new_games']) for r in results)
    
    if total_new == 0:
        body += "### ✅ 本次检测未发现新游戏\n\n"
    else:
        body += f"### 🎉 发现 {total_new} 个新游戏！\n\n"
    
    for result in results:
        body += f"### 📂 {result['display_name']}\n\n"
        body += f"- **总游戏数**: {result['total_games']}\n"
        body += f"- **新增游戏**: {len(result['new_games'])}\n\n"
        
        if result['new_games']:
            body += "**新游戏列表**:\n\n"
            for i, game in enumerate(result['new_games'], 1):
                body += f"{i}. [{game['name']}]({game['url']})\n"
            body += "\n"
        else:
            body += "*无新增游戏*\n\n"
    
    body += "---\n"
    body += "*此报告由 GitHub Actions 自动生成*\n"
    
    return body


def main():
    """主函数"""
    print("="*70)
    print("🔍 AZGames 监控系统")
    print("="*70)
    
    # 加载历史数据
    data = load_data()
    results = []
    has_new_games = False
    
    # 检查每个URL
    for url_config in URLS:
        category = url_config['name']
        url = url_config['url']
        display_name = url_config['display_name']
        
        print(f"\n正在检查: {display_name}")
        
        # 抓取当前游戏
        current_games = fetch_games(url)
        
        if not current_games:
            print(f"⚠️  未能抓取到数据")
            continue
        
        print(f"✓ 抓取到 {len(current_games)} 个游戏")
        
        # 获取历史数据
        old_games = data.get(category, [])
        
        # 查找新游戏
        new_games = find_new_games(old_games, current_games)
        
        if new_games:
            print(f"🎮 发现 {len(new_games)} 个新游戏！")
            has_new_games = True
            for game in new_games:
                print(f"  - {game['name']}")
        else:
            print(f"✓ 无新增游戏")
        
        # 更新数据
        data[category] = current_games
        
        # 记录结果
        results.append({
            'category': category,
            'display_name': display_name,
            'total_games': len(current_games),
            'new_games': new_games
        })
    
    # 保存数据
    save_data(data)
    
    # 生成报告
    report = create_issue_body(results)
    
    # 保存报告到文件
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # 保存状态（用于 GitHub Actions）
    with open('has_new_games.txt', 'w') as f:
        f.write('true' if has_new_games else 'false')
    
    print("\n" + "="*70)
    print(f"📊 检查完成")
    print(f"  - 检查了 {len(results)} 个分类")
    total_new = sum(len(r['new_games']) for r in results)
    print(f"  - 发现 {total_new} 个新游戏")
    print("="*70)
    
    return has_new_games


if __name__ == '__main__':
    main()
