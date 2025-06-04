import schedule
import time
from datetime import datetime
from fortune_analyzer import FortuneAnalyzer
from email_sender import EmailSender
from config import Config

class DailyFortuneService:
    """每日运势服务"""
    
    def __init__(self):
        self.analyzer = FortuneAnalyzer()
        self.email_sender = EmailSender()
        
    def send_daily_fortune(self):
        """发送每日运势"""
        try:
            print(f"🔮 开始生成每日运势... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # 分析运势
            fortune_content = self.analyzer.analyze_daily_fortune()
            
            # 发送邮件
            success = self.email_sender.send_fortune_email(fortune_content)
            
            if success:
                print("✅ 每日运势发送完成！")
                return True
            else:
                print("❌ 每日运势发送失败！")
                return False
                
        except Exception as e:
            print(f"❌ 服务执行出错: {e}")
            return False
    
    def test_service(self):
        """测试服务"""
        print("🧪 测试邮件配置...")
        
        try:
            # 验证配置
            Config.validate_config()
            print("✅ 配置验证通过")
            
            # 发送测试邮件
            if self.email_sender.send_test_email():
                print("✅ 测试邮件发送成功！")
                
                # 测试运势分析
                print("🔮 测试运势分析...")
                test_fortune = self.analyzer.analyze_daily_fortune()
                print("✅ 运势分析测试完成")
                
                return True
            else:
                print("❌ 测试邮件发送失败")
                return False
                
        except Exception as e:
            print(f"❌ 服务测试失败: {e}")
            return False
    
    def start_scheduler(self):
        """启动定时任务"""
        print(f"🚀 每日运势服务启动中...")
        print(f"⏰ 每日发送时间设置为: {Config.SEND_TIME}")
        print(f"👤 用户姓名: {Config.USER_NAME}")
        print(f"📧 邮件地址: {Config.EMAIL_USER}")
        
        # 设置定时任务
        schedule.every().day.at(Config.SEND_TIME).do(self.send_daily_fortune)
        
        print("✅ 定时任务已设置，服务正在运行...")
        print("💡 提示：按 Ctrl+C 停止服务")
        
        # 运行调度器
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # 每分钟检查一次
        except KeyboardInterrupt:
            print("\n👋 服务已停止")
    
    def send_now(self):
        """立即发送运势（用于测试）"""
        print("🚀 立即发送每日运势...")
        return self.send_daily_fortune()

def main():
    """主函数"""
    service = DailyFortuneService()
    
    print("=" * 50)
    print("🌟 每日运势邮件服务 🌟")
    print("=" * 50)
    
    while True:
        print("\n请选择操作：")
        print("1. 测试服务配置")
        print("2. 立即发送运势")
        print("3. 启动定时服务")
        print("4. 退出")
        
        choice = input("\n请输入选项 (1-4): ").strip()
        
        if choice == '1':
            service.test_service()
        elif choice == '2':
            service.send_now()
        elif choice == '3':
            service.start_scheduler()
            break
        elif choice == '4':
            print("👋 再见！")
            break
        else:
            print("❌ 无效选项，请重试")

if __name__ == "__main__":
    main() 