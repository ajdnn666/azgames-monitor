# 🚀 开始使用 - 3分钟部署指南

## ✅ 第一步：上传到 GitHub

```bash
# 在本目录打开终端，执行以下命令：

# 1. 初始化 Git
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "初始化 AZGames 监控系统"

# 4. 设置主分支
git branch -M main

# 5. 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/azgames-monitor.git

# 6. 推送到 GitHub
git push -u origin main
```

## ✅ 第二步：配置权限

1. 打开你的 GitHub 仓库
2. 点击 **Settings** → **Actions** → **General**
3. 找到 **Workflow permissions**
4. 选择 **Read and write permissions** ✓
5. 勾选 **Allow GitHub Actions to create and approve pull requests** ✓
6. 点击 **Save**

## ✅ 第三步：运行测试

1. 点击仓库顶部的 **Actions** 标签
2. 选择左侧的 **游戏监控** 工作流
3. 点击右侧的 **Run workflow** 按钮
4. 点击绿色的 **Run workflow** 确认
5. 等待1-2分钟，查看运行结果

## 🎉 完成！

系统现在会每小时自动运行，发现新游戏时会创建 GitHub Issue 通知你。

## 📬 接收通知

### 方法1：邮件通知（推荐）
- 进入 GitHub **Settings** → **Notifications**
- 确保 **Issues** 通知已启用
- 新游戏会发送到你的邮箱

### 方法2：移动应用
- 下载 GitHub App
- 登录后启用通知
- 实时接收推送

### 方法3：查看 Issues
- 直接访问仓库的 **Issues** 页面
- 查看所有新游戏记录

## 📖 详细文档

- **中文说明**：查看 `使用说明.md`
- **英文文档**：查看 `README.md`
- **部署指南**：查看 `setup.md`

## 🧪 本地测试（可选）

在推送到 GitHub 之前，可以先本地测试：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行测试
python test_local.py
```

## ❓ 遇到问题？

1. 查看 Actions 运行日志
2. 阅读 `使用说明.md` 中的常见问题
3. 在仓库创建 Issue 寻求帮助

---

**祝使用愉快！** 🎮
