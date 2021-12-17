import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
log = GetLog().get_logger()


class TestRent:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.rent_url)
        # 获取统一入口PageIn对象
        self.page_in = PageIn(driver)
        # 获取PageIn对象调用成功登录依赖方法
        # self.page_in.page_get_PageLogin().page_login_success()
        # 获取PageRent页面对象
        self.rent = self.page_in.page_get_PageRent()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_web_driver()

    # 新建测试租房业务方法
    def test_rent(self, values="金水区"):
        # 调用租房业务方法
        # 断言
        try:
            self.rent.page_rent(values)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.rent.base_get_image()
            # 抛出异常
            raise
