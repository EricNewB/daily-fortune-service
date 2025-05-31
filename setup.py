#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日运势服务安装和配置脚本
"""

import os
import shutil

def setup_service():
    """安装和配置服务"""
    print("🌟 每日运势服务安装程序 🌟")
    print("=" * 40)
    
    # 1. 检查配置文件
    if not os.path.exists('.env'):
        print("📁 创建配置文件...")
        shutil.copy('config_template.env', '.env')
        print("✅ 配置文件已创建：.env")
        print("⚠️  请编辑 .env 文件填写您的配置信息")
        return False
    
    # 2. 提示用户配置
    print("📋 请确保以下配置已正确填写：")
    print("   - DeepSeek API密钥")
    print("   - 邮箱账号和密码")
    print("   - 个人生辰八字信息")
    
    confirm = input("\n是否已完成配置？(y/n): ").lower()
    if confirm != 'y':
        print("❗ 请先完成配置后再运行服务")
        return False
    
    return True

def show_usage():
    """显示使用说明"""
    print("\n🎮 使用方法：")
    print("1. 测试模式：python daily_fortune_service.py")
    print("2. 直接启动：python run.py")
    print("3. 查看文档：README.md")

if __name__ == "__main__":
    if setup_service():
        show_usage()
        
        start_now = input("\n是否立即启动服务？(y/n): ").lower()
        if start_now == 'y':
            print("\n🚀 启动服务...")
            os.system('python run.py')
    else:
        print("\n💡 配置说明：")
        print("1. 编辑 .env 文件")
        print("2. 填写所有必要配置")
        print("3. 重新运行此脚本") 