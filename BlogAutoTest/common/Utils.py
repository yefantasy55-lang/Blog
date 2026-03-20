import datetime
import os
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 设置国内镜像源，避免访问 Google 服务器
os.environ['WDM_LOCAL'] = '0'
os.environ['CHROMEDRIVER_CDNURL'] = 'https://npmmirror.com/mirrors/chromedriver/'


def get_chrome_driver():
    # 检查 webdriver_manager 缓存目录
    cache_dir = os.path.join(os.path.expanduser('~'), '.wdm', 'drivers', 'chromedriver', 'win64')

    if os.path.exists(cache_dir):
        # 在缓存目录中查找最新版本的 chromedriver.exe
        import glob
        version_dirs = glob.glob(os.path.join(cache_dir, '*'))
        if version_dirs:
            latest_version = max(version_dirs)  # 取最新版本
            # 新版本可能在 chromedriver-win32 子目录
            subdirs = ['chromedriver-win32', 'chromedriver-win64']
            for subdir in subdirs:
                chromedriver_path = os.path.join(latest_version, subdir, 'chromedriver.exe')
                if os.path.exists(chromedriver_path):
                    return Service(executable_path=chromedriver_path)

    # 如果缓存没有，使用 webdriver_manager 自动下载
    print("未找到缓存的 ChromeDriver，正在自动下载...")
    driver_path = ChromeDriverManager().install()
    return Service(driver_path)


class BlogTest:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # 使用智能驱动加载，优先本地驱动
        self.driver = webdriver.Chrome(service=get_chrome_driver(), options=options)
        self.driver.implicitly_wait(10)  # 隐式等待

    # 弹窗
    def Alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())  # 显示等待弹窗
        return alert

    # 截图
    def ScreenShot(self, name):
        try:
            cur_time = datetime.datetime.now().strftime('%Y-%m-%d')
            dirname = "../images/" + cur_time  # 获取当前时间
            if not os.path.exists(dirname):  # 判断文件夹是否存在
                os.makedirs(dirname)
            filename = f"{dirname}/{name}_{datetime.datetime.now().strftime('%H时%M分%S秒')}.png"  # 根据传进来的名字，创建图片名称
            self.driver.get_screenshot_as_file(filename)  # 截屏并保存
            print(f"截图已保存：{filename}")
        except Exception as e:
            print(f"截图失败：{e}")

    # 清除输入框
    def clear(self):
        self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()

    # 退出
    def quit(self):
        self.driver.quit()

# 创建驱动对象
BlogDriver = BlogTest()
