#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
单次运行脚本 - 用于GitHub Actions
直接发送一次运势邮件，不使用定时器
"""

from daily_fortune_service import DailyFortuneService
import sys

def main():
    """单次运行函数"""
    print("🌟 GitHub Actions - 每日运势服务启动中...")
    
    try:
        service = DailyFortuneService()
        
        # 测试配置
        print("📋 正在验证配置...")
        if not service.test_service():
            print("❌ 配置验证失败")
            sys.exit(1)
        
        print("✅ 配置验证通过")
        
        # 直接发送运势邮件
        print("📧 正在发送运势邮件...")
        if service.send_daily_fortune():
            print("🎉 运势邮件发送成功！")
            sys.exit(0)
        else:
            print("❌ 运势邮件发送失败")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 