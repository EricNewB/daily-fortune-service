import requests
from config import Config

def check_deepseek_balance():
    """检查DeepSeek账户余额状态"""
    print("💰 检查DeepSeek账户余额状态...")
    print("=" * 50)
    
    api_key = Config.DEEPSEEK_API_KEY
    base_url = Config.DEEPSEEK_BASE_URL
    
    if not api_key:
        print("❌ API key未配置")
        return
    
    # 尝试发送一个简单的测试请求
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    test_data = {
        'model': 'deepseek-chat',
        'messages': [{'role': 'user', 'content': '测试'}],
        'max_tokens': 10
    }
    
    try:
        response = requests.post(
            f'{base_url}/chat/completions',
            headers=headers,
            json=test_data,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ 账户余额充足，API调用正常")
        elif response.status_code == 402:
            print("❌ 账户余额不足")
            print("\n📝 解决方案：")
            print("1. 访问 https://platform.deepseek.com/")
            print("2. 登录您的账户")
            print("3. 进入账户管理页面")
            print("4. 为账户充值")
            print("\n💡 DeepSeek的计费很便宜，通常几元钱就能使用很久")
        elif response.status_code == 401:
            print("❌ API key无效或过期")
        else:
            print(f"❓ 未知状态：HTTP {response.status_code}")
            print(f"响应：{response.text}")
            
    except Exception as e:
        print(f"❌ 检查失败：{e}")

if __name__ == "__main__":
    check_deepseek_balance() 