"""
本地测试脚本 - 用于测试爬虫和监控功能
"""
from scraper import fetch_games
from config import URLS


def test_scraper():
    """测试爬虫功能"""
    print("="*70)
    print("🧪 测试爬虫功能")
    print("="*70)
    
    for url_config in URLS:
        print(f"\n📂 测试: {url_config['display_name']}")
        print(f"🔗 URL: {url_config['url']}")
        
        games = fetch_games(url_config['url'])
        
        if games:
            print(f"✅ 成功抓取 {len(games)} 个游戏")
            print(f"\n前5个游戏:")
            for i, game in enumerate(games[:5], 1):
                print(f"  {i}. {game['name']}")
                print(f"     {game['url']}")
        else:
            print(f"❌ 抓取失败")
        
        print("-"*70)
    
    print("\n✅ 爬虫测试完成！\n")


def test_monitor():
    """测试完整监控流程"""
    print("="*70)
    print("🧪 测试监控流程")
    print("="*70)
    
    from monitor import main
    
    try:
        main()
        print("\n✅ 监控测试完成！")
        print("\n📝 检查以下文件:")
        print("  - games_data.json (游戏数据)")
        print("  - report.md (检测报告)")
        print("  - has_new_games.txt (是否有新游戏)")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎮 AZGames 监控系统 - 本地测试")
    print("="*70 + "\n")
    
    # 测试爬虫
    test_scraper()
    
    # 测试监控
    print("\n")
    test_monitor()
    
    print("\n" + "="*70)
    print("✅ 所有测试完成！")
    print("="*70 + "\n")
