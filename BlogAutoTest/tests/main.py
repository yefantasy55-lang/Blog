import time

from BlogAutoTest.common.Utils import BlogDriver
from BlogAutoTest.tests.BlogDetailTest import BlogDetail
from BlogAutoTest.tests.BlogEditTest import BlogEdit
from BlogAutoTest.tests.BlogLoginTest import BlogLogin
from BlogAutoTest.tests.BlogListTest import BlogList

if __name__ == "__main__":
    # 登录测试
    BlogLogin().login_fail()
    BlogLogin().login_success()

    # 博客列表测试
    BlogList().blog_list_succes()

    # 博客编辑测试
    BlogEdit().edit_success()

    # 博客详情页测试
    BlogDetail().detail_success()

    # 退出
    BlogDriver.quit()