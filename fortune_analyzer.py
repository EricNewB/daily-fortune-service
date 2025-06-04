import requests
import json
from datetime import datetime, date, timezone, timedelta
from config import Config

class FortuneAnalyzer:
    """运势分析器"""
    
    def __init__(self):
        self.api_key = Config.DEEPSEEK_API_KEY
        self.base_url = Config.DEEPSEEK_BASE_URL
        # 设置韩国时区 (UTC+9)
        self.korea_tz = timezone(timedelta(hours=9))
        
    def get_korea_time(self):
        """获取韩国时间"""
        return datetime.now(self.korea_tz)
    
    def get_bazi_info(self, user_info=None):
        """获取生辰八字信息"""
        if user_info:
            return {
                '出生年': user_info.get('birth_year'),
                '出生月': user_info.get('birth_month'),
                '出生日': user_info.get('birth_day'),
                '出生时': user_info.get('birth_hour'),
                '性别': user_info.get('birth_gender', '男')
            }
        return {
            '出生年': Config.BIRTH_YEAR,
            '出生月': Config.BIRTH_MONTH,
            '出生日': Config.BIRTH_DAY,
            '出生时': Config.BIRTH_HOUR,
            '性别': Config.BIRTH_GENDER
        }
    
    def create_fortune_prompt(self, today_date, user_info=None):
        """创建运势分析提示词"""
        bazi_info = self.get_bazi_info(user_info)
        user_name = user_info.get('user_name') if user_info else Config.USER_NAME

        prompt = f"""
你是一位专业的周易命理师，请根据以下信息为用户分析今日运势：

个人信息：
- 姓名：{user_name}
- 出生年月日：{bazi_info['出生年']}年{bazi_info['出生月']}月{bazi_info['出生日']}日{bazi_info['出生时']}时
- 性别：{bazi_info['性别']}
- 今日日期：{today_date}

请提供以下内容的详细分析：

1. **今日整体运势**（评分1-10分）
2. **事业运势**：工作方面的建议和注意事项
3. **财运分析**：财务方面的运势和理财建议
4. **感情运势**：人际关系和感情方面的指导
5. **健康运势**：身体健康方面的提醒
6. **今日宜做**：适合今天做的事情（3-5项）
7. **今日忌做**：今天应该避免的事情（3-5项）
8. **幸运色彩**：今日的幸运色
9. **幸运数字**：今日的幸运数字
10. **每日贴士**：一句积极正面的人生建议

请用温馨友好的语气，条理清晰地进行分析，让用户感到温暖和鼓励。
"""
        return prompt
    
    def analyze_daily_fortune(self, user_info=None):
        """分析每日运势"""
        try:
            korea_time = self.get_korea_time()
            today = korea_time.strftime('%Y年%m月%d日')
            user_name = user_info.get('user_name') if user_info else Config.USER_NAME
            print(f"🔍 开始分析运势... 用户: {user_name} 日期: {today} (韩国时间)")
            
            # 检查API key配置
            if not self.api_key or self.api_key == 'your_deepseek_api_key_here':
                print("❌ 错误：DeepSeek API key未配置或使用默认值")
                return self.get_fallback_fortune(today, user_info)
            
            print(f"🔑 API Key配置检查通过 (长度: {len(self.api_key)})")
            
            prompt = self.create_fortune_prompt(today, user_info)
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': 'deepseek-chat',
                'messages': [
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'temperature': 0.7,
                'max_tokens': 2000
            }
            
            print(f"🌐 正在调用DeepSeek API: {self.base_url}/chat/completions")
            
            response = requests.post(
                f'{self.base_url}/chat/completions',
                headers=headers,
                json=data,
                timeout=30
            )
            
            print(f"📡 API响应状态码: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                fortune_content = result['choices'][0]['message']['content']
                print("✅ API调用成功，已获取运势内容")
                return self.format_fortune_content(fortune_content, today, user_info)
            else:
                print(f"❌ API调用失败: {response.status_code}")
                print(f"📄 响应内容: {response.text}")
                return self.get_fallback_fortune(today, user_info)
                
        except requests.exceptions.Timeout:
            print("❌ API调用超时")
            return self.get_fallback_fortune(today, user_info)
        except requests.exceptions.ConnectionError:
            print("❌ 网络连接错误")
            return self.get_fallback_fortune(today, user_info)
        except Exception as e:
            print(f"❌ 分析运势时出错: {e}")
            print(f"📝 错误类型: {type(e).__name__}")
            return self.get_fallback_fortune(today, user_info)
    
    def format_fortune_content(self, content, today, user_info=None):
        """格式化运势内容"""
        korea_time = self.get_korea_time()
        user_name = user_info.get('user_name') if user_info else Config.USER_NAME
        formatted_content = f"""
🌟 {user_name}的每日运势 - {today} 🌟

{content}

━━━━━━━━━━━━━━━━━━━━━━━━━━━
💫 愿您今天拥有美好的一天！
由DeepSeek AI智能分析提供 | 生成时间：{korea_time.strftime('%Y-%m-%d %H:%M:%S KST')}
"""
        return formatted_content
    
    def get_fallback_fortune(self, today, user_info=None):
        """备用运势内容（API调用失败时使用）"""
        user_name = user_info.get('user_name') if user_info else Config.USER_NAME
        return f"""
🌟 {user_name}的每日运势 - {today} 🌟

**今日整体运势**：7/10分
今天是平稳发展的一天，保持积极的心态，会有不错的收获。

**事业运势**：工作中保持专注，与同事合作愉快。
**财运分析**：财运平稳，适合制定理财计划。
**感情运势**：人际关系和谐，适合表达关心。
**健康运势**：注意休息，保持规律作息。

**今日宜做**：
• 处理重要工作
• 与朋友交流
• 学习新知识
• 整理生活环境

**今日忌做**：
• 冲动消费
• 熬夜晚睡
• 与人争执

**幸运色彩**：蓝色
**幸运数字**：7

**每日贴士**：保持微笑，世界会因你而更美好！

━━━━━━━━━━━━━━━━━━━━━━━━━━━
💫 愿您今天拥有美好的一天！
⚠️ 备用运势内容（API连接失败）| 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""" 