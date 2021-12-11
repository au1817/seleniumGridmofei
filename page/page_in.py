from page.page_app_login import PageAppLogin
from page.page_app_rent import PageAppRent
from page.page_center import PageCenter
from page.page_login import PageLogin
from page.page_rent import PageRent


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageLogin对象
    def page_get_PageLogin(self):
        return PageLogin(self.driver)

    # 获取PageRent对象
    def page_get_PageRent(self):
        return PageRent(self.driver)

    # 获取PageCenter对象
    def page_get_PageCenter(self):
        return PageCenter(self.driver)

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppRent对象
    def page_get_PageAppRent(self):
        return PageAppRent(self.driver)