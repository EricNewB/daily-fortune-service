#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日运势服务启动脚本
"""

from daily_fortune_service import DailyFortuneService

def main():
    """简化的启动函数"""
    print("🌟 每日运势服务启动中...")
    
    service = DailyFortuneService()
    
    # 先测试配置
    if service.test_service():
        print("\n🎉 配置测试通过！正在启动定时服务...")
        service.start_scheduler()
    else:
        print("\n❌ 配置测试失败，请检查配置后重试")

if __name__ == "__main__":
    main() 