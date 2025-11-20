# 🚀 快速部署指南

## 步骤 1: 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 **+** → **New repository**
3. 填写仓库信息：
   - **Repository name**: `azgames-monitor` (或其他名称)
   - **Description**: `AZGames 游戏监控系统`
   - **Public** 或 **Private** (推荐 Private)
4. 点击 **Create repository**

## 步骤 2: 推送代码到 GitHub

在本地项目目录打开终端，执行以下命令：

```bash
# 初始化 Git 仓库（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "初始化 AZGames 监控系统"

# 设置主分支
git branch -M main

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/azgames-monitor.git

# 推送到 GitHub
git push -u origin main
```

## 步骤 3: 配置 GitHub Actions 权限

1. 进入你的 GitHub 仓库页面
2. 点击 **Settings** (设置)
3. 在左侧菜单找到 **Actions** → **General**
4. 滚动到 **Workflow permissions** 部分
5. 选择 **Read and write permissions** (读写权限)
6. 勾选 **Allow GitHub Actions to create and approve pull requests**
7. 点击 **Save** (保存)

## 步骤 4: 首次运行测试

### 方法 1: 手动触发

1. 点击仓库顶部的 **Actions** 标签
2. 在左侧选择 **游戏监控** 工作流
3. 点击右侧的 **Run workflow** 按钮
4. 点击绿色的 **Run workflow** 确认
5. 等待几分钟，查看运行结果

### 方法 2: 等待自动运行

- GitHub Actions 会在每小时的整点自动运行
- 首次运行会建立基准数据
- 之后的运行会检测新游戏

## 步骤 5: 查看结果

### 查看运行日志

1. 进入 **Actions** 标签
2. 点击最新的运行记录
3. 查看详细日志

### 查看新游戏通知

1. 进入 **Issues** 标签
2. 当发现新游戏时，会自动创建 Issue
3. 你会收到邮件或移动通知（需要在 GitHub 设置中启用）

## 步骤 6: 启用通知（可选）

### 邮件通知

1. 进入 GitHub 账户 **Settings** → **Notifications**
2. 确保 **Email** 通知已启用
3. 勾选 **Issues** 相关的通知选项

### 移动通知

1. 下载 GitHub 移动应用 (iOS/Android)
2. 登录你的账户
3. 启用推送通知
4. 当有新 Issue 时会收到推送

## 🎉 完成！

现在系统会每小时自动监控三个网址，发现新游戏时会通过 GitHub Issue 通知你。

## 📊 验证系统是否正常工作

运行成功的标志：

- ✅ Actions 标签页显示绿色的勾号
- ✅ `games_data.json` 文件被更新
- ✅ 如果有新游戏，会创建新的 Issue

## ⚠️ 常见问题

### Q: Actions 显示红色 X 失败了怎么办？

**A**: 点击失败的运行记录，查看错误日志。常见原因：
- 权限设置不正确
- 网络无法访问目标网站
- Python 依赖安装失败

### Q: 为什么没有创建 Issue？

**A**: 可能的原因：
- 首次运行只会建立基准数据，不会创建 Issue
- 确实没有新游戏
- 检查 Actions 日志确认是否检测到新游戏

### Q: 如何修改监控频率？

**A**: 编辑 `.github/workflows/monitor.yml` 文件中的 cron 表达式：

```yaml
# 每小时
- cron: '0 * * * *'

# 每2小时
- cron: '0 */2 * * *'

# 每天早上9点
- cron: '0 1 * * *'  # UTC时间，北京时间需要+8
```

### Q: 如何停止监控？

**A**: 两种方法：
1. 删除 `.github/workflows/monitor.yml` 文件
2. 在仓库 Settings → Actions → General 中禁用 Actions

## 🔧 高级配置

### 添加更多监控网址

编辑 `config.py` 文件，在 `URLS` 列表中添加新的网址。

### 自定义通知内容

编辑 `monitor.py` 文件中的 `create_issue_body()` 函数。

### 修改数据存储方式

默认使用 JSON 文件存储在仓库中。如需使用数据库，可以修改 `monitor.py` 中的存储逻辑。

## 📞 需要帮助？

如有问题，请在仓库中创建 Issue 描述你遇到的问题。
