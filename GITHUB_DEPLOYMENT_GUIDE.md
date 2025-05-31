# 🌟 GitHub每日运势服务部署指南

## 📁 文件上传清单

请将以下文件上传到您的GitHub仓库（`EricNewB/daily-fortune-service`）：

### 🔧 核心服务文件
- ✅ `daily_fortune_service.py` - 主服务文件
- ✅ `fortune_analyzer.py` - 运势分析模块  
- ✅ `email_sender.py` - 邮件发送模块
- ✅ `config.py` - 配置管理模块
- ✅ `single_run.py` - GitHub Actions专用运行脚本

### 📦 配置和依赖
- ✅ `requirements.txt` - Python依赖包
- ✅ `config_template.env` - 环境变量模板

### 🤖 GitHub Actions工作流
- ✅ `.github/workflows/daily-fortune.yml` - 自动化工作流

### 📚 文档文件
- ✅ `README.md` - 项目说明（已更新）
- ✅ `DEPLOYMENT.md` - 部署指南

## 🚀 快速部署步骤

### 步骤1：上传文件

有两种方式：

#### 方式A：使用Git命令行（推荐）
```bash
# 克隆您的仓库
git clone https://github.com/EricNewB/daily-fortune-service.git
cd daily-fortune-service

# 将项目文件复制到仓库目录
# 然后执行：
git add .
git commit -m "🌟 Add complete daily fortune service"
git push origin main
```

#### 方式B：GitHub网页上传
1. 进入您的GitHub仓库页面
2. 点击 "Add file" → "Upload files"
3. 拖拽所有项目文件到页面
4. 填写提交信息：`🌟 Add complete daily fortune service`
5. 点击 "Commit changes"

### 步骤2：配置GitHub Secrets

在GitHub仓库中设置Secrets：
`Settings → Secrets and variables → Actions → New repository secret`

#### 必需配置：
| Secret名称 | 说明 | 示例值 |
|-----------|------|--------|
| `DEEPSEEK_API_KEY` | DeepSeek API密钥 | `sk-xxxxx...` |
| `EMAIL_USER` | 发送邮箱地址 | `your@qq.com` |
| `EMAIL_PASSWORD` | 邮箱授权码 | `abcdxxxx` |
| `BIRTH_YEAR` | 出生年份 | `1990` |
| `BIRTH_MONTH` | 出生月份 | `5` |
| `BIRTH_DAY` | 出生日期 | `15` |
| `BIRTH_HOUR` | 出生时辰 | `14` |

#### 可选配置：
| Secret名称 | 说明 | 默认值 |
|-----------|------|--------|
| `SMTP_SERVER` | SMTP服务器 | `smtp.qq.com` |
| `SMTP_PORT` | SMTP端口 | `587` |
| `USER_NAME` | 称呼 | `朋友` |
| `BIRTH_GENDER` | 性别 | `男` |
| `SEND_TIME` | 发送时间 | `08:00` |

### 步骤3：测试运行

1. 进入仓库的 `Actions` 页面
2. 选择 `Daily Fortune Service` 工作流
3. 点击 `Run workflow` 按钮
4. 点击绿色的 `Run workflow` 确认
5. 等待运行完成（约1-2分钟）
6. 检查邮箱是否收到运势邮件

### 步骤4：自动化确认

✅ **自动运行时间**：每天早上8点（韩国时间KST）  
✅ **监控地址**：GitHub仓库的Actions页面  
✅ **结果确认**：检查邮箱中的运势邮件  

## 📧 重要配置说明

### QQ邮箱配置（推荐）
```
SMTP_SERVER=smtp.qq.com
SMTP_PORT=587
EMAIL_USER=your@qq.com
EMAIL_PASSWORD=授权码（不是QQ密码）
```

### 获取QQ邮箱授权码：
1. 登录QQ邮箱网页版
2. 设置 → 账户 → 开启SMTP服务
3. 生成授权码（需要手机验证）
4. 将16位授权码填入 `EMAIL_PASSWORD` Secret

### 获取DeepSeek API密钥：
1. 访问 https://www.deepseek.com
2. 注册/登录账号
3. 进入API管理页面
4. 创建新的API密钥
5. 确保账户有足够余额

## 🔍 故障排除

### Actions运行失败
1. 查看Actions页面的详细日志
2. 检查Secrets配置是否完整
3. 确认DeepSeek API余额是否充足
4. 验证邮箱配置是否正确

### 邮件未收到
1. 检查垃圾邮件文件夹
2. 确认邮箱授权码是否有效
3. 查看Actions运行日志中的错误信息

### API调用失败
1. 检查DeepSeek API密钥是否正确
2. 确认API账户余额是否充足
3. 查看网络连接是否正常

## 🎉 部署完成

部署成功后，您将：
- ✅ 每天早上8点（韩国时间）自动收到个性化运势邮件
- ✅ 可以在GitHub Actions页面监控运行状态
- ✅ 可以手动触发发送运势邮件
- ✅ 享受完全免费的自动化服务

## 📱 下一步

1. **个性化定制**：修改 `fortune_analyzer.py` 中的提示词
2. **邮件样式**：调整 `email_sender.py` 中的HTML模板
3. **发送时间**：修改workflow文件中的cron表达式
4. **通知方式**：可以添加更多通知渠道

---

🌟 **愿好运每天伴随您！GitHub自动化让运势服务更加便捷！** 🌟 