# 🎮 AZGames 游戏监控系统

自动监控 AZGames 网站的新游戏，每小时检测一次，发现新游戏时自动创建 GitHub Issue 通知。

## 📋 功能特点

- ✅ 每小时自动监控三个游戏分类
- ✅ 自动检测新增游戏
- ✅ 通过 GitHub Issue 推送通知
- ✅ 完全基于 GitHub Actions，无需服务器
- ✅ 自动保存历史数据

## 🔗 监控的网址

1. **热门趋势游戏**: https://azgames.io/trending-games
2. **火爆游戏**: https://azgames.io/hot-games
3. **流行游戏**: https://azgames.io/popular-games

## 🚀 快速开始

### 1. Fork 或克隆此仓库

```bash
git clone <your-repo-url>
cd monitoring
```

### 2. 推送到 GitHub

```bash
git init
git add .
git commit -m "初始化游戏监控系统"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 3. 启用 GitHub Actions

1. 进入你的 GitHub 仓库
2. 点击 **Settings** → **Actions** → **General**
3. 在 **Workflow permissions** 部分，选择 **Read and write permissions**
4. 勾选 **Allow GitHub Actions to create and approve pull requests**
5. 点击 **Save**

### 4. 手动触发测试（可选）

1. 进入 **Actions** 标签页
2. 选择 **游戏监控** 工作流
3. 点击 **Run workflow** 按钮
4. 等待运行完成

## 📊 工作原理

```
┌─────────────────────────────────────────────────────────┐
│  GitHub Actions (每小时触发)                              │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  1. 抓取三个网址的游戏列表                                 │
│  2. 与历史数据对比                                        │
│  3. 识别新增游戏                                          │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
                    有新游戏？
                    /        \
                 是 /          \ 否
                   /            \
                  ▼              ▼
    ┌──────────────────┐   ┌──────────────┐
    │ 创建 GitHub Issue│   │ 仅更新数据    │
    │ 发送通知          │   │              │
    └──────────────────┘   └──────────────┘
                  │              │
                  └──────┬───────┘
                         ▼
            ┌────────────────────────┐
            │ 更新 games_data.json   │
            │ 提交到仓库              │
            └────────────────────────┘
```

## 📁 项目结构

```
monitoring/
├── .github/
│   └── workflows/
│       └── monitor.yml          # GitHub Actions 工作流配置
├── config.py                    # 配置文件
├── scraper.py                   # 网页爬虫模块
├── monitor.py                   # 监控主程序
├── games_data.json              # 游戏数据存储（自动生成）
├── requirements.txt             # Python 依赖
├── .gitignore                   # Git 忽略文件
└── README.md                    # 项目文档
```

## ⚙️ 配置说明

### 修改监控间隔

编辑 `.github/workflows/monitor.yml` 文件中的 cron 表达式：

```yaml
on:
  schedule:
    - cron: '0 * * * *'  # 每小时运行
    # - cron: '0 */2 * * *'  # 每2小时运行
    # - cron: '0 */6 * * *'  # 每6小时运行
```

### 添加或修改监控网址

编辑 `config.py` 文件中的 `URLS` 列表：

```python
URLS = [
    {
        'name': 'trending-games',
        'url': 'https://azgames.io/trending-games',
        'display_name': '热门趋势游戏'
    },
    # 添加更多URL...
]
```

## 📬 接收通知

当系统检测到新游戏时，会自动创建一个 GitHub Issue，包含：

- 🎮 新游戏的名称和链接
- 📊 每个分类的统计信息
- 🕐 检测时间

### 启用邮件通知

1. 进入 GitHub 仓库的 **Settings** → **Notifications**
2. 确保 **Issues** 的通知已启用
3. GitHub 会自动发送邮件到你的注册邮箱

### 启用移动通知

1. 安装 GitHub 移动应用
2. 登录你的账号
3. 启用通知权限
4. 当有新 Issue 时会收到推送

## 🧪 本地测试

```bash
# 安装依赖
pip install -r requirements.txt

# 运行一次监控
python monitor.py
```

## 📝 查看历史记录

所有检测到的新游戏都会记录在：

1. **GitHub Issues** - 每次发现新游戏都会创建一个 Issue
2. **games_data.json** - 保存所有游戏的最新状态
3. **Actions 日志** - 每次运行的详细日志

## 🔧 故障排查

### Actions 没有运行

1. 检查 Actions 是否已启用
2. 检查工作流权限是否正确设置
3. 查看 Actions 标签页的错误日志

### 没有收到通知

1. 检查 GitHub 通知设置
2. 确认邮箱地址正确
3. 检查垃圾邮件文件夹

### 数据没有更新

1. 查看 Actions 运行日志
2. 检查 `games_data.json` 是否有写入权限
3. 确认网络可以访问目标网站

## 📊 监控数据示例

`games_data.json` 文件格式：

```json
{
  "trending-games": [
    {
      "name": "Slope Rider",
      "url": "https://azgames.io/slope-rider"
    }
  ],
  "hot-games": [...],
  "popular-games": [...]
}
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🔗 相关链接

- [AZGames 官网](https://azgames.io/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [BeautifulSoup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

**提示**: 首次运行时，所有现有游戏都会被记录为基准数据，之后只会通知新增的游戏。
