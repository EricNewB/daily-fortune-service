import schedule
import time
from datetime import datetime, timezone, timedelta
from fortune_analyzer import FortuneAnalyzer
from email_sender import EmailSender
from config import Config

class DailyFortuneService:
    """每日运势服务"""
    
    def __init__(self):
        self.analyzer = FortuneAnalyzer()
        self.email_sender = EmailSender()
        # 设置韩国时区 (UTC+9)
        self.korea_tz = timezone(timedelta(hours=9))
        
    def get_korea_time(self):
        """获取韩国时间"""
        return datetime.now(self.korea_tz)
    
    def send_daily_fortune(self):
        """发送每日运势"""
        try:
            users = Config.get_users()
            korea_time = self.get_korea_time()
            all_success = True
            for user in users:
                print(
                    f"🔮 开始生成每日运势... {korea_time.strftime('%Y-%m-%d %H:%M:%S KST')} 用户: {user.get('user_name')}"
                )

                fortune_content = self.analyzer.analyze_daily_fortune(user)

                success = self.email_sender.send_fortune_email(
                    fortune_content,
                    user.get('email'),
                    user.get('user_name'),
                )

                if success:
                    print(f"✅ 已向 {user.get('email')} 发送运势")
                else:
                    print(f"❌ 向 {user.get('email')} 发送失败")
                    all_success = False

            return all_success
                
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
            
            users = Config.get_users()
            all_success = True
            for user in users:
                if self.email_sender.send_test_email(user.get('email'), user.get('user_name')):
                    print(f"✅ 测试邮件已发送至 {user.get('email')}")
                else:
                    print(f"❌ 测试邮件发送至 {user.get('email')} 失败")
                    all_success = False

                print("🔮 测试运势分析...")
                self.analyzer.analyze_daily_fortune(user)

            return all_success
                
        except Exception as e:
            print(f"❌ 服务测试失败: {e}")
            return False
    
    def start_scheduler(self):
        """启动定时任务"""
        print(f"🚀 每日运势服务启动中...")
        print(f"⏰ 每日发送时间设置为: {Config.SEND_TIME}")
        users = Config.get_users()
        for u in users:
            print(f"👤 用户姓名: {u.get('user_name')} | 邮件: {u.get('email')}")
        
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