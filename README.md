# 🌟 每日运势邮件服务

这是一个基于DeepSeek AI的每日运势分析服务，可以根据您的生辰八字每天自动发送个性化的运势邮件。

## ✨ 功能特点

- 🤖 **AI智能分析**: 使用DeepSeek API进行专业的生辰八字运势分析
- 📧 **精美邮件**: 自动发送HTML格式的精美运势邮件
- ⏰ **定时发送**: 支持自定义每日发送时间
- 🎯 **个性化**: 基于您的生辰八字进行个性化分析
- 🛡️ **安全可靠**: 支持环境变量配置，保护隐私信息

## 📋 运势内容

每日运势包含以下详细分析：

- 📊 **整体运势评分** (1-10分)
- 💼 **事业运势** - 工作建议和注意事项
- 💰 **财运分析** - 财务运势和理财建议
- 💕 **感情运势** - 人际关系指导
- 🏥 **健康运势** - 身体健康提醒
- ✅ **今日宜做** - 适合今天做的事情
- ❌ **今日忌做** - 今天应该避免的事情
- 🎨 **幸运色彩** - 今日幸运色
- 🔢 **幸运数字** - 今日幸运数字
- 💡 **每日贴士** - 积极正面的人生建议

## 🚀 快速开始

### 部署方式选择

我们提供两种部署方式：

#### 🌐 方式一：GitHub自动部署（推荐）
- ✅ 完全免费
- ✅ 自动每日运行
- ✅ 无需本地服务器
- ✅ 高可靠性

请参阅 [DEPLOYMENT.md](DEPLOYMENT.md) 了解详细部署步骤。

#### 🖥️ 方式二：本地部署

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制配置模板并填写您的信息：

```bash
cp config_template.env .env
```

编辑 `.env` 文件，填写以下信息：

```env
# DeepSeek API配置
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# 邮件配置
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here

# 个人信息配置
USER_NAME=你的姓名
BIRTH_YEAR=1990
BIRTH_MONTH=1
BIRTH_DAY=1
BIRTH_HOUR=8
BIRTH_GENDER=男

# 运势发送时间（24小时制）
SEND_TIME=08:00
```

### 3. 运行服务

```bash
python daily_fortune_service.py
```

## 🔧 配置说明

### DeepSeek API配置

1. 访问 [DeepSeek官网](https://www.deepseek.com) 注册账号
2. 获取API密钥
3. 将密钥填入 `DEEPSEEK_API_KEY`

### 邮件配置

#### Gmail配置示例
1. 开启两步验证
2. 生成应用专用密码
3. 使用应用专用密码作为 `EMAIL_PASSWORD`

#### 其他邮箱配置
- **QQ邮箱**: `smtp.qq.com:587`
- **163邮箱**: `smtp.163.com:587`
- **Outlook**: `smtp-mail.outlook.com:587`

### 生辰八字配置

- `BIRTH_YEAR`: 出生年份（公历）
- `BIRTH_MONTH`: 出生月份（1-12）
- `BIRTH_DAY`: 出生日期（1-31）
- `BIRTH_HOUR`: 出生时辰（0-23）
- `BIRTH_GENDER`: 性别（男/女）

### 多用户配置

如果需要向多位用户发送运势邮件，可创建 `users_config.json` 文件，并在 `.env` 中设置 `USERS_FILE` 指向该文件。文件示例：

```json
[
  {
    "email": "659521082@qq.com",
    "user_name": "Chen",
    "birth_year": "1997",
    "birth_month": "2",
    "birth_day": "3",
    "birth_hour": "14",
    "birth_gender": "男"
  },
  {
    "email": "2267542935@qq.com",
    "user_name": "User2",
    "birth_year": "1998",
    "birth_month": "5",
    "birth_day": "12",
    "birth_hour": "8",
    "birth_gender": "女"
  },
  {
    "email": "2242650683@qq.com",
    "user_name": "朱朱",
    "birth_year": "1995",
    "birth_month": "10",
    "birth_day": "12",
    "birth_hour": "3",
    "birth_gender": "女"
  }
]
```

配置该文件后，程序会根据每位用户的生辰八字分别生成并发送邮件。

## 🎮 使用方法

运行程序后会出现菜单：

```
🌟 每日运势邮件服务 🌟

请选择操作：
1. 测试服务配置
2. 立即发送运势
3. 启动定时服务
4. 退出
```

### 选项说明

1. **测试服务配置**: 验证配置并发送测试邮件
2. **立即发送运势**: 立即生成并发送今日运势
3. **启动定时服务**: 启动定时任务，每日自动发送
4. **退出**: 退出程序

## 📁 项目结构

```
cursor_normal/
├── daily_fortune_service.py    # 主服务文件
├── fortune_analyzer.py         # 运势分析模块
├── email_sender.py             # 邮件发送模块
├── config.py                   # 配置管理模块
├── requirements.txt            # 项目依赖
├── config_template.env         # 配置模板
└── README.md                   # 项目说明
```

## 🔍 故障排除

### 常见问题

1. **邮件发送失败**
   - 检查邮箱账号密码是否正确
   - 确认是否使用了应用专用密码
   - 检查SMTP服务器配置

2. **DeepSeek API调用失败**
   - 确认API密钥是否正确
   - 检查网络连接
   - 查看API额度是否充足

3. **配置验证失败**
   - 检查 `.env` 文件是否存在
   - 确认所有必要字段都已填写

### 日志信息

程序运行时会显示详细的日志信息：
- ✅ 表示操作成功
- ❌ 表示操作失败
- 🔮 表示正在分析运势
- 📧 表示邮件相关操作

## 🌈 定制化

您可以根据需要修改以下内容：

- **邮件模板**: 编辑 `email_sender.py` 中的HTML模板
- **运势分析**: 修改 `fortune_analyzer.py` 中的提示词
- **发送频率**: 修改定时任务设置

## 📝 许可证

本项目采用 MIT 许可证。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如果您在使用过程中遇到问题，请：

1. 查看故障排除部分
2. 检查配置是否正确
3. 查看控制台日志信息

---

�� **愿好运每天伴随您！** 🌟 