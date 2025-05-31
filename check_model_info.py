import requests
from config import Config

def check_current_model():
    """检查当前使用的模型信息"""
    print("🤖 当前模型信息")
    print("=" * 50)
    
    # 显示当前配置的模型
    print("📍 当前运势服务使用的模型：")
    print("   模型代码：deepseek-chat")
    print("   实际版本：DeepSeek-V3-0324")
    print("   发布日期：2025年3月25日")
    print("   特点：强大的对话和创作能力，适合运势分析")
    
    print("\n🔄 可选模型：")
    print("1. deepseek-chat (当前使用)")
    print("   - 版本：DeepSeek-V3-0324")
    print("   - 适用：对话、创作、分析")
    print("   - 推荐：运势分析 ✅")
    
    print("\n2. deepseek-reasoner")
    print("   - 版本：DeepSeek-R1-0528") 
    print("   - 适用：复杂推理、逻辑分析")
    print("   - 推荐：数学问题、逻辑推理")

def test_model_response():
    """测试当前模型的响应"""
    print("\n🧪 测试当前模型响应")
    print("=" * 50)
    
    api_key = Config.DEEPSEEK_API_KEY
    base_url = Config.DEEPSEEK_BASE_URL
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    test_data = {
        'model': 'deepseek-chat',
        'messages': [
            {
                'role': 'user',
                'content': '请用一句话介绍你自己，包括你的模型版本信息。'
            }
        ],
        'max_tokens': 100
    }
    
    try:
        response = requests.post(
            f'{base_url}/chat/completions',
            headers=headers,
            json=test_data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            print(f"🤖 模型自我介绍：")
            print(f"   {content}")
            
            # 显示详细的使用信息
            if 'usage' in result:
                usage = result['usage']
                print(f"\n📊 本次调用使用情况：")
                print(f"   输入tokens：{usage.get('prompt_tokens', 'N/A')}")
                print(f"   输出tokens：{usage.get('completion_tokens', 'N/A')}")
                print(f"   总计tokens：{usage.get('total_tokens', 'N/A')}")
            
            # 显示响应中的模型信息
            if 'model' in result:
                print(f"\n🏷️  API返回的模型标识：{result['model']}")
        else:
            print(f"❌ 测试失败：{response.status_code}")
            
    except Exception as e:
        print(f"❌ 测试错误：{e}")

if __name__ == "__main__":
    check_current_model()
    test_model_response()
    
    print("\n" + "=" * 50)
    print("💡 如需切换模型，可以修改 fortune_analyzer.py 中的 'model' 参数")
    print("   当前推荐继续使用 deepseek-chat，它最适合运势分析任务") 