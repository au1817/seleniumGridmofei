import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_logger()


# 新建类
class TestAppRent:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_app_driver()
        # 获取捅咕一入口对象
        self.page_in = PageIn(driver)
        # 调用登录方法

        # 获取查找地铁线路方法
        self.rent = self.page_in.page_get_PageAppRent()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_app_driver()

    # 新建测试方法
    @pytest.mark.parametrize("click_text, title", read_yaml("app_rent_room.yaml"))
    def test_app_rent(self, click_text, title):
        try:
            # 调用查找地铁线陆业务方法
            self.rent.page_app_rent(click_text, title)
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、截图
            self.rent.base_get_image()
            # 3、抛出异常
            raise
