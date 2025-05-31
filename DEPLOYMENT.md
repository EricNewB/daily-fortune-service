# GitHub 每日运势服务部署指南

## 🚀 部署步骤

### 1. 创建GitHub仓库

1. 登录您的GitHub账号
2. 创建一个新的仓库（例如：`daily-fortune-service`）
3. 将本项目代码上传到仓库

### 2. 配置GitHub Secrets

在GitHub仓库中配置以下Secrets（Settings → Secrets and variables → Actions → New repository secret）：

#### 必需配置：
- `DEEPSEEK_API_KEY`: 您的DeepSeek API密钥
- `EMAIL_USER`: 发送邮件的邮箱地址
- `EMAIL_PASSWORD`: 邮箱的应用专用密码
- `BIRTH_YEAR`: 出生年份（如：1990）
- `BIRTH_MONTH`: 出生月份（如：5）
- `BIRTH_DAY`: 出生日期（如：15）
- `BIRTH_HOUR`: 出生时辰（如：14）

#### 可选配置：
- `SMTP_SERVER`: SMTP服务器（默认：smtp.qq.com）
- `SMTP_PORT`: SMTP端口（默认：587）
- `USER_NAME`: 称呼（默认：朋友）
- `BIRTH_GENDER`: 性别（默认：男）
- `SEND_TIME`: 发送时间（默认：08:00）

### 3. 时区说明

GitHub Actions使用UTC时间，当前设置为UTC 23:00运行，对应：
- 韩国时间：08:00 (KST, UTC+9)
- 北京时间：07:00 (CST, UTC+8)
- 如需调整时间，修改`.github/workflows/daily-fortune.yml`中的cron表达式

### 4. 手动测试

部署完成后，您可以：
1. 进入Actions页面
2. 选择"Daily Fortune Service"工作流
3. 点击"Run workflow"手动触发测试

## 📅 运行时间表

- **自动运行**：每天早上8点（韩国时间KST）
- **手动运行**：随时可在Actions页面手动触发

## 🔍 监控和日志

- 在Actions页面可以查看每次运行的详细日志
- 成功/失败状态会在Actions页面显示
- 可以通过邮箱接收运势结果来确认服务正常

## ⚠️ 注意事项

1. **API配额**：注意DeepSeek API的使用限制
2. **邮箱安全**：使用应用专用密码，不要使用账号登录密码
3. **Secrets安全**：不要在代码中硬编码敏感信息
4. **网络稳定性**：GitHub Actions的网络环境可能影响API调用

## 🐛 故障排除

### 常见问题：

1. **邮件发送失败**
   - 检查SMTP配置是否正确
   - 确认邮箱应用专用密码是否有效

2. **API调用失败**
   - 检查DeepSeek API密钥是否正确
   - 确认API账户余额是否充足

3. **时间不准确**
   - 检查GitHub Actions的时区设置
   - 可能需要等待下一个整点才会运行

### 调试方法：

1. 查看Actions运行日志
2. 手动触发workflow进行测试
3. 检查Secrets配置是否完整

## 📞 支持

如遇问题，请检查：
1. GitHub Actions运行日志
2. 邮箱中是否收到运势邮件
3. DeepSeek API账户状态 