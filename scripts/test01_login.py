# 导包
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


# 新建类 并继承
class TestLogin:
    # setup_class方法
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.login_url)
        # 2、通过统一入口类获取PageLogin对象
        self.login = PageIn(driver).page_get_PageLogin()
        pass

    # teardown_class方法
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 新建测试业务方法
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("login.yaml"))
    def test_login(self, username, pwd, expect):
        # 调用登录业务方法
        self.login.page_login(username, pwd)
        # 断言
        try:
            result = self.login.page_get_nickname()
            assert result == expect
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            print("错误原因：", e)
            self.login.page_get_image()
            raise


