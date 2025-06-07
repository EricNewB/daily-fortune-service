import os
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置管理类"""
    
    # DeepSeek API配置
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

    # OpenAI API配置（备用）
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    
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

    USERS_FILE = os.getenv('USERS_FILE')  # 可选的多用户配置文件路径

    @classmethod
    def get_users(cls):
        """获取用户列表"""
        if cls.USERS_FILE and os.path.exists(cls.USERS_FILE):
            try:
                with open(cls.USERS_FILE, 'r', encoding='utf-8') as f:
                    users = json.load(f)
                if isinstance(users, list):
                    return users
            except Exception as e:
                print(f"❌ 读取用户配置文件失败: {e}")

        # 回退到单用户配置
        return [{
            'email': cls.EMAIL_USER,
            'user_name': cls.USER_NAME,
            'birth_year': cls.BIRTH_YEAR,
            'birth_month': cls.BIRTH_MONTH,
            'birth_day': cls.BIRTH_DAY,
            'birth_hour': cls.BIRTH_HOUR,
            'birth_gender': cls.BIRTH_GENDER,
        }]
    
    @classmethod
    def validate_config(cls):
        """验证配置是否完整"""
        if not cls.DEEPSEEK_API_KEY:
            raise ValueError("缺少必要配置: DEEPSEEK_API_KEY")

        if not cls.OPENAI_API_KEY:
            print("⚠️ 未设置OPENAI_API_KEY，将在DeepSeek失败时使用本地备用内容")

        if cls.USERS_FILE and os.path.exists(cls.USERS_FILE):
            users = cls.get_users()
            if not users:
                raise ValueError("用户配置文件为空或格式错误")
            for u in users:
                for key in [
                    'email', 'user_name', 'birth_year',
                    'birth_month', 'birth_day', 'birth_hour'
                ]:
                    if not u.get(key):
                        raise ValueError(f"用户配置缺少字段: {key}")
        else:
            required_fields = [
                'EMAIL_USER', 'EMAIL_PASSWORD',
                'BIRTH_YEAR', 'BIRTH_MONTH', 'BIRTH_DAY', 'BIRTH_HOUR'
            ]
            missing_fields = []
            for field in required_fields:
                if not getattr(cls, field):
                    missing_fields.append(field)
            if missing_fields:
                raise ValueError(f"缺少必要配置: {', '.join(missing_fields)}")

        return True
