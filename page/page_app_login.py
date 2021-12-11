from time import sleep
import page
from base.app_base import AppBase
from tools.get_log import GetLog
log = GetLog().get_logger()


class PageAppLogin(AppBase):
    # 1、点击菜单我的
    def page_click_my(self):
        sleep(1)
        self.base_click(page.app_my)

    # 2、点击头像进入登录页面
    def page_click_image(self):
        sleep(1)
        self.base_click(page.app_image)

    # 3、切换账号登录
    def page_account_login(self):
        sleep(1)
        self.base_click(page.app_account)

    # 4、输入用户名
    def page_input_phone(self, phone):
        sleep(1)
        self.base_input(page.app_phone, phone)

    # 5、输入密码
    def page_input_pwd(self, pwd):
        sleep(1)
        self.base_input(page.app_pwd, pwd)

    # 6.、点击登录按钮
    def page_click_login_btn(self):
        sleep(2)
        self.base_click(page.app_login_btn)

    # 7、判断账号是否存在 账号名称
    def page_is_login_success(self):
        sleep(1)
        return self.app_base_id_exit(page.app_nickname)

    # 8、组合登录业务方法
    def page_app_login(self, phone, pwd):
        log.info("正在调用app应用登录业务方法 手机号：{}  密码：{}".format(phone, pwd))
        self.page_click_my()
        self.page_click_image()
        self.page_account_login()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

   # 组合登录业务方法 -查找地铁线路 登录成功依赖方法
    def page_app_login_success(self, phone="17875512080", pwd="au123456"):
        log.info("正在调用app应用登录业务方法 手机号：{}  密码：{}".format(phone, pwd))
        self.page_click_my()
        self.page_click_image()
        self.page_account_login()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()