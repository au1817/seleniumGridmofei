# 导包
from time import sleep
import page
from base.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from tools.get_log import GetLog
log = GetLog.get_logger()


# 新建类
class PageLogin(Base):
    # 点击“登录”链接
    def page_login_link(self):
        self.base_click(page.login_link)

    # 点击“账号密码登录”链接
    def page_userandpwd_link(self):
        self.base_click(page.login_userandpwd_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录按钮
    def page_login_btn(self):
        try:
            sleep(1)
            self.base_click(page.login_btn)
            # el = self.base_find(page.login_btn)
            # print(el.get_attribute('outerHTML'))
            # result = el.is_enabled()
            # print(result)
            # el.click()
            # el.click()
            # self.driver.execute_script("argument[0].click();", el)
            # js = 'return document.getElementsByClassName("login-user-tel-btn")[2].click()'
            # self.driver.execute_script(js)

            # self.driver.execute_script('document.getElementsByClassName(" login-user-tel-btn")[0].click()')

            # el = self.base_find(page.login_btn)
            # # print("登录按钮", self.base_get_text(page.login_btn))
            # my_action = ActionChains(self.driver)
            # my_action.move_to_element(el).perform()

            # self.base_click(page.login_btn)
        except Exception as e:
            print("异常信息：", e)
            raise

    # # 点击"置业管家"刷新
    # def page_click_butler(self):
    #     sleep(3)
    #     self.base_click(page.login_butler)

    # 获取昵称
    def page_get_nickname(self):
        sleep(1)
        return self.base_get_text(page.login_nickname)

    # 截图
    def page_get_image(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, pwd):
        log.info("正在调用登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_login_link()
        self.page_userandpwd_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_login_btn()

    # 组合业务方法->租房业务依赖使用
    def page_login_success(self, username="17875512080", pwd="au123456"):
        log.info("正在调用登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_login_link()
        self.page_userandpwd_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_login_btn()


