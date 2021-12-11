import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
log = GetLog().get_logger()


class TestCenter:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_web_driver(page.login_url)
        # 调用PageIn统一入口对象
        self.page_in = PageIn(driver)
        # 调用登录成功依赖方法
        self.page_in.page_get_PageLogin().page_login_success()
        # 调用PageCenter页面对象
        self.center = self.page_in.page_get_PageCenter()

    # 结束
    def teardown_class(self):
        GetDriver().quit_web_driver()

    # 新建测试批量删除业务方法
    def test_center(self):
        # 调用批量删除业务方法
        self.center.page_all_del()
        # 断言
        print("属性信息为：", self.center.page_search_picture())
