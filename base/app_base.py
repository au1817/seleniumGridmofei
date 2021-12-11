from selenium.webdriver.common.by import By
from base.base import Base
from selenium.common.exceptions import NoSuchElementException
from tools.get_log import GetLog
log = GetLog().get_logger()


class AppBase(Base):
    # 查找页面是否存在指定元素
    def app_base_id_exit(self, loc):
        try:
            # 1、调用查找方法 定时3秒
            self.base_find(loc, timeout=3)
            log.info("在app页面中找到指定元素!")
            # 2、输出信息
            print("找到：{}元素啦！".format(loc))
            # 返回True
            return True
        except:
            log.error("没有在app页面中找到指定元素")
            # 1、输出信息
            print("未找到：{}元素！".format(loc))
            # 2、返回False
            return False

    # 从右到左滑动屏幕
    def app_base_right_swipe_left(self, loc_area, click_text):
        log.info("正在调用 从右到左滑动方法")
        # 1、查找区域元素
        el = self.base_find(loc_area)
        # 2、获取区域元素的位置的 Y坐标
        y = el.location.get("y")
        # 3、获取区域元素的宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4、计算 start_x, start_y, end_x, end_y
        start_x = width * 0.8
        start_y = height * 0.5 + y
        end_x = width * 0.2
        end_y = height * 0.5 + y

        # 组合元素配置信息
        loc = By.XPATH, "//android.widget.LinearLayout/*[contains(@text,'{}')]".format(click_text)
        # loc = By.XPATH, "//*[@text='{}' and @class='android.widget.TextView']".format(click_text)
        # loc = By.XPATH, "//*[@text='{}' and @class='android.widget.TextView']".format(click_text)
        # 5、循环操作
        while True:
            # 1、获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2、捕获异常
            try:
                # 1、查找元素
                log.info("正要查找：{}元素".format(loc))
                self.base_find(loc, timeout=3)
                # 2、输出提示信息
                print("找到：{}元素啦！".format(loc))
                # 3、点击元素
                self.base_click(loc)
                # 4、跳出循环
                break
            # 3、处理异常
            except:
                # 1、输出提示信息
                print("未找到：{}元素！".format(loc))
                # 2、滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4、判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1、输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 2、抛出未找到元素异常
                raise NoSuchElementException

    # 从下到上滑动屏幕
    def app_base_down_swipe_up(self, loc_area, click_text):
        log.info("正在调用 从下到上滑动方法")
        # 1、查找区域元素
        el = self.base_find(loc_area)
        # 3、获取区域元素的宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4、计算 start_x, start_y, end_x, end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 组合元素配置信息
        loc = By.XPATH, "//*[@class='android.support.v7.widget.RecyclerView']//*[contains(@text,'{}')]".format(click_text)
        # 5、循环操作
        while True:
            # 1、获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2、捕获异常
            try:
                # 1、查找元素
                log.info("正要查找：{}元素".format(loc))
                self.base_find(loc, timeout=3)
                # 2、输出提示信息
                print("找到：{}元素啦！".format(loc))
                # 3、点击元素
                self.base_click(loc)
                # 4、跳出循环
                break
            # 3、处理异常
            except:
                # 1、输出提示信息
                print("未找到：{}元素！".format(loc))
                # 2、滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4、判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1、输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 2、抛出未找到元素异常
                raise NoSuchElementException