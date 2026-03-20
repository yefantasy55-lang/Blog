# 博客编辑页自动化测试

from BlogAutoTest.common.Utils import BlogDriver
from selenium.webdriver.common.by import By

class BlogEdit:
    def __init__(self):
        self.url = "http://47.108.157.13:8090/blog_edit.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    # 成功编辑
    def edit_success(self):
        # 测试按键功能
        self.driver.find_element(By.CSS_SELECTOR, "#editor > div.editormd-toolbar > div > ul > li:nth-child(12) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, "#editor > div.editormd-toolbar > div > ul > li:nth-child(12) > a").click()

        # 测试发布和编辑功能
        self.driver.find_element(By.CSS_SELECTOR, "#title").send_keys("测试标题")  # 标题
        BlogDriver.ScreenShot("编辑成功")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click() # 提交

        # 查看是否成功发布
        BlogDriver.Alert().accept()
        name = self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3").text
        assert name == "zhangsan"
        BlogDriver.ScreenShot("发布成功")

