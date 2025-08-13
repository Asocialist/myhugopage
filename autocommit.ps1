# autocommit.ps1

# --- 1. 获取当前时间并格式化 ---
# 获取当前日期和时间对象
$now = Get-Date
# 定义你想要的时间格式，例如 "年-月-日 小时:分钟:秒"
$timestamp = $now.ToString("yyyy-MM-dd HH:mm:ss")

# --- 2. 构建提交信息 ---
# 将固定文本和时间戳组合成最终的提交信息
$commitMessage = "website update $timestamp"

# --- 3. 执行 Git 命令 ---

# 打印提示信息，告诉用户正在做什么
Write-Host "第一步：正在将所有更改添加到暂存区 (git add .)..."
# 执行 git add 命令
git add .
# 检查上一步是否成功
if (-not $?) { Write-Host "错误：'git add' 命令失败！"; exit 1 }

# 打印将要使用的提交信息
Write-Host "第二步：正在提交更改，提交信息为: '$commitMessage'..."
# 执行 git commit 命令
git commit -m "$commitMessage"
# 检查上一步是否成功
if (-not $?) { Write-Host "错误：'git commit' 命令失败！可能是没有需要提交的更改。"; exit 1 }

# 打印提示信息
Write-Host "第三步：正在推送到远程仓库 (git push)..."
# 执行 git push 命令
git push
# 检查上一步是否成功
if (-not $?) { Write-Host "错误：'git push' 命令失败！"; exit 1 }

# --- 4. 完成 ---
Write-Host "操作成功完成！"