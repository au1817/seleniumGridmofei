from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog
log = GetLog().get_logger()


# 新建web_base类 继承Base
class WebBase(Base):
    # 根据显示文本点击指定元素
    def web_base_click_element(self, direction, direction_text):
        # 点击复选框
        loc = By.XPATH, "//span[text()='{}']".format(direction)
        log.info("正在对：{}元素点击复选框".format(loc))
        self.base_click(loc)
        # 点击包含文本显示的元素
        loc = By.XPATH, "//a[text()='{}']".format(direction_text)
        log.info("正在点击包含文本显示：{}元素".format(loc))
        self.base_click(loc)

    # 刷新窗口操作
    def web_base_refresh(self):
        log.info("正在刷新窗口")
        self.driver.refresh()
