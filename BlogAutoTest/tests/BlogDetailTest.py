# 博客详情页自动化测试
from selenium.webdriver.common.by import By

from common.Utils import BlogDriver

class BlogDetail:
    def __init__(self):
        self.url = "http://47.108.157.13:8090/blog_detail.html?blogId=70950"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def detail_success(self):
        text=self.driver.find_element(By.CSS_SELECTOR, "#detail > p").text  # 博客内容
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3")  # 博客作者
        assert text == "测试03"
        BlogDriver.ScreenShot("博客详情成功")