import time

from common.Utils import BlogDriver
from tests.BlogDetailTest import BlogDetail
from tests.BlogEditTest import BlogEdit
from tests.BlogLoginTest import BlogLogin
from tests.BlogListTest import BlogList

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