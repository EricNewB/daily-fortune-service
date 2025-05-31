import requests
import json
from config import Config

def test_deepseek_api():
    """测试DeepSeek API连接"""
    print("🔍 开始测试DeepSeek API连接...")
    print("=" * 50)
    
    # 检查API key配置
    api_key = Config.DEEPSEEK_API_KEY
    base_url = Config.DEEPSEEK_BASE_URL
    
    print(f"📍 API Base URL: {base_url}")
    
    if not api_key:
        print("❌ 错误：DEEPSEEK_API_KEY 未设置")
        print("📝 请在 .env 文件中设置您的DeepSeek API key")
        return False
    
    if api_key == 'your_deepseek_api_key_here':
        print("❌ 错误：仍在使用默认的API key模板")
        print("📝 请在 .env 文件中替换为真实的DeepSeek API key")
        return False
    
    print(f"🔑 API Key已配置 (长度: {len(api_key)})")
    print(f"🔑 API Key前缀: {api_key[:10]}...")
    
    # 测试API调用
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    test_data = {
        'model': 'deepseek-chat',
        'messages': [
            {
                'role': 'user',
                'content': '你好，请简单回复一下，这是一个API连接测试。'
            }
        ],
        'temperature': 0.7,
        'max_tokens': 50
    }
    
    try:
        print("\n🌐 发送测试请求到DeepSeek API...")
        response = requests.post(
            f'{base_url}/chat/completions',
            headers=headers,
            json=test_data,
            timeout=30
        )
        
        print(f"📡 响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            print("✅ API连接成功！")
            print(f"📄 API响应: {content}")
            
            # 检查usage信息
            if 'usage' in result:
                usage = result['usage']
                print(f"💰 Token使用情况:")
                print(f"   - 输入tokens: {usage.get('prompt_tokens', 'N/A')}")
                print(f"   - 输出tokens: {usage.get('completion_tokens', 'N/A')}")
                print(f"   - 总计tokens: {usage.get('total_tokens', 'N/A')}")
            
            return True
            
        else:
            print(f"❌ API调用失败: HTTP {response.status_code}")
            print(f"📄 错误响应: {response.text}")
            
            # 分析常见错误
            if response.status_code == 401:
                print("💡 可能原因：API key无效或过期")
            elif response.status_code == 403:
                print("💡 可能原因：API key没有权限或账户余额不足")
            elif response.status_code == 429:
                print("💡 可能原因：请求频率过高，需要等待")
            elif response.status_code >= 500:
                print("💡 可能原因：DeepSeek服务器错误，请稍后重试")
            
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 请求超时")
        print("💡 可能原因：网络连接慢或DeepSeek服务器响应慢")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ 连接错误")
        print("💡 可能原因：网络连接问题或DNS解析失败")
        return False
        
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        print(f"📝 错误类型: {type(e).__name__}")
        return False

def check_env_file():
    """检查环境变量文件"""
    import os
    
    print("\n📁 检查环境变量文件...")
    
    if os.path.exists('.env'):
        print("✅ 找到 .env 文件")
        with open('.env', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'DEEPSEEK_API_KEY=' in content:
                lines = content.split('\n')
                for line in lines:
                    if line.strip().startswith('DEEPSEEK_API_KEY='):
                        key_part = line.split('=', 1)[1] if '=' in line else ''
                        if key_part and key_part != 'your_deepseek_api_key_here':
                            print("✅ DEEPSEEK_API_KEY 已设置")
                        else:
                            print("❌ DEEPSEEK_API_KEY 未正确设置")
                        break
            else:
                print("❌ .env 文件中没有找到 DEEPSEEK_API_KEY")
    else:
        print("❌ 未找到 .env 文件")
        print("💡 请创建 .env 文件并配置您的API key")

if __name__ == "__main__":
    check_env_file()
    print("\n" + "=" * 50)
    success = test_deepseek_api()
    print("\n" + "=" * 50)
    
    if success:
        print("🎉 DeepSeek API连接测试成功！")
        print("💡 现在您的运势服务应该可以正常工作了")
    else:
        print("❌ DeepSeek API连接测试失败")
        print("💡 请按照上面的提示解决问题后重新测试") 