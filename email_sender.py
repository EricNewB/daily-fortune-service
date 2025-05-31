import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import re
from config import Config

class EmailSender:
    """邮件发送器"""
    
    def __init__(self):
        self.smtp_server = Config.SMTP_SERVER
        self.smtp_port = Config.SMTP_PORT
        self.email_user = Config.EMAIL_USER
        self.email_password = Config.EMAIL_PASSWORD
    
    def send_fortune_email(self, fortune_content):
        """发送运势邮件"""
        try:
            # 创建邮件对象
            msg = MIMEMultipart()
            msg['From'] = self.email_user  # QQ邮箱要求简单格式
            msg['To'] = self.email_user
            
            today = datetime.now().strftime('%Y年%m月%d日')
            msg['Subject'] = Header(f"🌟 {Config.USER_NAME}的每日运势 - {today}", 'utf-8')
            
            # 邮件正文
            html_content = self.create_html_content(fortune_content)
            msg.attach(MIMEText(html_content, 'html', 'utf-8'))
            
            # 连接SMTP服务器并发送邮件
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # 启用安全传输
            server.login(self.email_user, self.email_password)
            
            text = msg.as_string()
            server.sendmail(self.email_user, [self.email_user], text)
            server.quit()
            
            print(f"✅ 运势邮件发送成功！发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
            
        except Exception as e:
            print(f"❌ 邮件发送失败：{e}")
            return False
    
    def markdown_to_html(self, text):
        """将markdown格式转换为HTML"""
        # 处理markdown标题 ### -> <h3>
        text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
        text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
        text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
        
        # 处理markdown分隔线 --- 或 ***
        text = re.sub(r'^---+$', '<hr>', text, flags=re.MULTILINE)
        text = re.sub(r'^\*\*\*+$', '<hr>', text, flags=re.MULTILINE)
        
        # 处理粗体 **text** -> <strong>text</strong>
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        
        # 处理斜体 *text* -> <em>text</em>
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        
        # 处理列表项 • -> 🔸, - -> 🔸
        text = text.replace('• ', '🔸 ')
        text = re.sub(r'^- (.*?)$', r'🔸 \1', text, flags=re.MULTILINE)
        
        # 处理我们自己的分隔线
        text = text.replace('━━━━━━━━━━━━━━━━━━━━━━━━━━━', '<hr>')
        
        # 处理段落
        paragraphs = text.split('\n\n')
        html_paragraphs = []
        
        for para in paragraphs:
            if para.strip():
                # 跳过已经是HTML标签的内容
                if para.strip().startswith('<h') or para.strip() == '<hr>':
                    html_paragraphs.append(para)
                # 检查是否是标题（包含**的行或emoji开头）
                elif ('**' in para and len(para.split('\n')) == 1) or para.startswith('🌟') or para.startswith('💫'):
                    html_paragraphs.append(f'<div class="section-title">{para}</div>')
                else:
                    # 处理普通段落中的换行
                    para_lines = para.split('\n')
                    formatted_lines = []
                    for line in para_lines:
                        if line.strip():
                            # 跳过HTML标签
                            if line.strip().startswith('<'):
                                formatted_lines.append(line)
                            elif line.startswith('🔸') or line.strip().startswith('🔸'):
                                formatted_lines.append(f'<div class="list-item">{line}</div>')
                            else:
                                formatted_lines.append(f'<div class="content-line">{line}</div>')
                    if formatted_lines:
                        html_paragraphs.append('<div class="content-section">' + ''.join(formatted_lines) + '</div>')
        
        return ''.join(html_paragraphs)
    
    def create_html_content(self, fortune_content):
        """创建HTML格式的邮件内容"""
        # 转换markdown内容为HTML
        formatted_content = self.markdown_to_html(fortune_content)
        
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日运势</title>
    <style>
        body {{
            font-family: 'Microsoft YaHei', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 650px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 25px;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 15px;
            border: 3px solid #f8f9fa;
        }}
        .header h1 {{
            color: #d63384;
            margin: 0;
            font-size: 28px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }}
        .header p {{
            color: #6f42c1;
            margin: 10px 0 0 0;
            font-size: 16px;
            font-style: italic;
        }}
        .content {{
            font-size: 16px;
            line-height: 1.8;
            color: #2c3e50;
        }}
        .section-title {{
            font-size: 20px;
            font-weight: bold;
            color: #e91e63;
            margin: 25px 0 15px 0;
            padding: 10px 15px;
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 10px;
            border-left: 5px solid #e91e63;
        }}
        .content-section {{
            margin: 15px 0;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 3px solid #17a2b8;
        }}
        .content-line {{
            margin: 8px 0;
            padding: 5px 0;
        }}
        .list-item {{
            margin: 8px 0;
            padding: 8px 15px;
            background: white;
            border-radius: 8px;
            border-left: 3px solid #28a745;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 25px;
            background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
            border-radius: 15px;
            font-size: 14px;
            color: #6c757d;
            border: 2px solid #e9ecef;
        }}
        .footer p {{
            margin: 8px 0;
        }}
        .emoji {{
            font-size: 18px;
            margin: 0 5px;
        }}
        strong {{
            color: #dc3545;
            font-weight: bold;
        }}
        em {{
            color: #6f42c1;
            font-style: italic;
        }}
        h1, h2, h3 {{
            color: #e91e63;
            margin: 20px 0 10px 0;
            padding: 8px 12px;
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 8px;
            border-left: 4px solid #e91e63;
        }}
        h1 {{
            font-size: 22px;
        }}
        h2 {{
            font-size: 20px;
        }}
        h3 {{
            font-size: 18px;
        }}
        hr {{
            border: none;
            height: 3px;
            background: linear-gradient(to right, #ffecd2, #fcb69f);
            margin: 25px 0;
            border-radius: 2px;
        }}
        .highlight {{
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><span class="emoji">🌟</span> 每日运势提醒 <span class="emoji">🌟</span></h1>
            <p>愿美好的运势伴您一整天 ✨</p>
        </div>
        
        <div class="content">
            {formatted_content}
        </div>
        
        <div class="footer">
            <p><span class="emoji">🤖</span> 由 <span class="highlight">EricChen AIlab</span> 智能分析提供</p>
            <p><span class="emoji">📧</span> 如需修改配置，请联系管理员</p>
            <p><span class="emoji">⏰</span> 发送时间：{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}</p>
            <p><span class="emoji">💝</span> 祝您今天心情愉快，万事如意！</p>
        </div>
    </div>
</body>
</html>
        """
        return html_template
    
    def send_test_email(self):
        """发送测试邮件"""
        test_content = f"""
🌟 {Config.USER_NAME}的每日运势测试 - {datetime.now().strftime('%Y年%m月%d日')} 🌟

🧪 **这是一封测试邮件**

亲爱的{Config.USER_NAME}，您好！

这是每日运势服务的测试邮件。如果您收到了这封邮件，说明邮件配置正确！

**测试项目：**
🔸 邮件是否正常接收
🔸 HTML格式是否正确显示
🔸 中文是否正常显示
🔸 emoji表情是否显示正常

**今日测试运势：**
🔸 **整体运势**：测试顺利，配置成功！
🔸 **技术运势**：代码运行良好，bug远离！
🔸 **心情运势**：看到美丽邮件，心情愉悦！

━━━━━━━━━━━━━━━━━━━━━━━━━━━
💫 如果一切正常，每日运势服务就可以开始工作了！
        """
        
        return self.send_fortune_email(test_content) 