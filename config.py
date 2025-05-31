import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置管理类"""
    
    # DeepSeek API配置
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
    
    # 邮件配置
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')  # 默认Gmail
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # 应用专用密码
    
    # 个人信息配置
    USER_NAME = os.getenv('USER_NAME', '朋友')
    BIRTH_YEAR = os.getenv('BIRTH_YEAR')
    BIRTH_MONTH = os.getenv('BIRTH_MONTH')
    BIRTH_DAY = os.getenv('BIRTH_DAY')
    BIRTH_HOUR = os.getenv('BIRTH_HOUR')
    BIRTH_GENDER = os.getenv('BIRTH_GENDER', '男')  # 男/女
    
    # 运势发送时间
    SEND_TIME = os.getenv('SEND_TIME', '08:00')  # 默认早上8点
    
    @classmethod
    def validate_config(cls):
        """验证配置是否完整"""
        required_fields = [
            'DEEPSEEK_API_KEY', 'EMAIL_USER', 'EMAIL_PASSWORD',
            'BIRTH_YEAR', 'BIRTH_MONTH', 'BIRTH_DAY', 'BIRTH_HOUR'
        ]
        
        missing_fields = []
        for field in required_fields:
            if not getattr(cls, field):
                missing_fields.append(field)
        
        if missing_fields:
            raise ValueError(f"缺少必要配置: {', '.join(missing_fields)}")
        
        return True 