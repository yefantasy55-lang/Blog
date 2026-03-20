# 博客首页自动化测试

from selenium.webdriver.common.by import By

from BlogAutoTest.common.Utils import BlogDriver

class BlogList:
    def __init__(self):
        self.url = "http://47.108.157.13:8090/blog_list.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)

    def blog_list_succes(self):
        BlogDriver.Alert().accept()
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > img")
        text=self.driver.find_element(By.CSS_SELECTOR, "body > div.nav > span").text
        BlogDriver.ScreenShot("博客成功展示")
        assert text=="我的博客系统"
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > a").click()
        BlogDriver.ScreenShot("博客文章按键正常")
