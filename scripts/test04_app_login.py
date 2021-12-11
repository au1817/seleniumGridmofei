import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog().get_logger()


# 新建类
class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取appdriver
        driver = GetDriver().get_app_driver()
        # 获取统一入口对象
        self.page_in = PageIn(driver)
        # 获取app登录业务对象
        self.app_login = self.page_in.page_get_PageAppLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_app_driver()

    # 新建测试app登录业务方法
    @pytest.mark.parametrize("phone, pwd", read_yaml("app_login.yaml"))
    def test_app_login(self, phone, pwd):
        # 调用app登录业务方法
        self.app_login.page_app_login(phone, pwd)
        try:
            # 断言
            assert self.app_login.page_is_login_success()
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、截图
            self.app_login.base_get_image()
            # 3、抛异常
            raise
