from email_sender import EmailSender

def main():
    print("📧 发送测试邮件...")
    sender = EmailSender()
    success = sender.send_test_email()
    
    if success:
        print("✅ 测试邮件发送成功！请检查您的邮箱")
    else:
        print("❌ 测试邮件发送失败")

if __name__ == "__main__":
    main() 