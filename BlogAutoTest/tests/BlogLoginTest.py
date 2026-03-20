# 博客登录页自动化测试
import time

from selenium.webdriver.common.by import By

from common.Utils import BlogDriver


class BlogLogin:
    def __init__(self):
        self.url = "http://47.108.157.13:8090/blog_login.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    # 成功登录
    def login_success(self):
        # 清除输入框
        BlogDriver.clear()
        # 输入用户名和密码
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        BlogDriver.ScreenShot("登录界面")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        # 跳转到登录成功页面
        alert=BlogDriver.Alert()
        alert.accept()
        name = self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3").text
        assert name == "zhangsan"
        BlogDriver.ScreenShot("登录成功")

    def login_fail(self):
        # 清除输入框
        BlogDriver.clear()
        # 输入用户名和密码
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("admin")  # 用户名错误
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        alert = BlogDriver.Alert()
        text = alert.text
        assert text == "用户不存在"
        alert.accept()
        BlogDriver.ScreenShot("登录失败-用户名错误")

        # 清除输入框
        BlogDriver.clear()
        # 输入用户名和密码
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123")  # 密码错误
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        alert = BlogDriver.Alert()
        assert alert.text == "密码错误"
        alert.accept()
        BlogDriver.ScreenShot("登录失败-密码错误")

