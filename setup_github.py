#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GitHub仓库设置脚本
帮助用户快速设置GitHub仓库
"""

import os
import sys

def print_banner():
    """打印横幅"""
    print("=" * 60)
    print("🌟 每日运势服务 - GitHub自动部署设置向导")
    print("=" * 60)
    print()

def print_step(step_num, title):
    """打印步骤标题"""
    print(f"\n📋 步骤 {step_num}: {title}")
    print("-" * 40)

def main():
    """主函数"""
    print_banner()
    
    print("本脚本将指导您完成GitHub仓库的设置。")
    print("请确保您已经：")
    print("✅ 拥有GitHub账号")
    print("✅ 准备好DeepSeek API密钥")
    print("✅ 准备好邮箱配置信息")
    print()
    
    input("按回车键继续...")
    
    print_step(1, "创建GitHub仓库")
    print("1. 登录GitHub (https://github.com)")
    print("2. 点击右上角的 '+' → 'New repository'")
    print("3. 仓库名建议：daily-fortune-service")
    print("4. 设置为Public（免费账户需要公开仓库才能使用Actions）")
    print("5. 勾选 'Add a README file'")
    print("6. 点击 'Create repository'")
    print()
    input("完成后按回车键继续...")
    
    print_step(2, "上传项目代码")
    print("将当前目录的所有文件上传到GitHub仓库：")
    print()
    print("方法一 - 使用Git命令行：")
    print("  git init")
    print("  git add .")
    print("  git commit -m \"Initial commit\"")
    print("  git branch -M main")
    print("  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git")
    print("  git push -u origin main")
    print()
    print("方法二 - 使用GitHub网页：")
    print("  1. 在GitHub仓库页面点击 'uploading an existing file'")
    print("  2. 拖拽所有项目文件到页面")
    print("  3. 填写提交信息")
    print("  4. 点击 'Commit changes'")
    print()
    input("完成后按回车键继续...")
    
    print_step(3, "配置GitHub Secrets")
    print("在GitHub仓库中设置以下Secrets：")
    print("路径：Settings → Secrets and variables → Actions → New repository secret")
    print()
    
    secrets = [
        ("DEEPSEEK_API_KEY", "您的DeepSeek API密钥"),
        ("EMAIL_USER", "发送邮件的邮箱地址"),
        ("EMAIL_PASSWORD", "邮箱的应用专用密码"),
        ("BIRTH_YEAR", "出生年份（如：1990）"),
        ("BIRTH_MONTH", "出生月份（如：5）"),
        ("BIRTH_DAY", "出生日期（如：15）"),
        ("BIRTH_HOUR", "出生时辰（如：14）"),
    ]
    
    print("必需配置的Secrets：")
    for name, desc in secrets:
        print(f"  📌 {name}: {desc}")
    
    print()
    print("可选配置的Secrets：")
    optional_secrets = [
        ("SMTP_SERVER", "SMTP服务器（默认：smtp.qq.com）"),
        ("SMTP_PORT", "SMTP端口（默认：587）"),
        ("USER_NAME", "称呼（默认：朋友）"),
        ("BIRTH_GENDER", "性别（默认：男）"),
        ("SEND_TIME", "发送时间（默认：08:00）"),
    ]
    
    for name, desc in optional_secrets:
        print(f"  📝 {name}: {desc}")
    
    print()
    input("完成后按回车键继续...")
    
    print_step(4, "测试运行")
    print("1. 进入仓库的 'Actions' 页面")
    print("2. 选择 'Daily Fortune Service' 工作流")
    print("3. 点击 'Run workflow' 按钮")
    print("4. 点击绿色的 'Run workflow' 确认")
    print("5. 等待运行完成（约1-2分钟）")
    print("6. 检查邮箱是否收到运势邮件")
    print()
    
    print_step(5, "完成设置")
    print("🎉 恭喜！您的每日运势服务已经设置完成！")
    print()
    print("📅 自动运行时间：每天早上8点（北京时间）")
    print("🔍 监控地址：GitHub仓库的Actions页面")
    print("📧 结果确认：检查邮箱中的运势邮件")
    print()
    print("⚠️  重要提醒：")
    print("- 确保DeepSeek API账户有足够余额")
    print("- 定期检查GitHub Actions运行状态")
    print("- 如有问题请查看Actions运行日志")
    print()
    print("🌟 愿好运每天伴随您！")

if __name__ == "__main__":
    main() 