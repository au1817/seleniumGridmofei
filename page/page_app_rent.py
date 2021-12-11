import page
from base.app_base import AppBase
from tools.get_log import GetLog
log = GetLog().get_logger()

class PageAppRent(AppBase):
    # 1、点击 地铁沿线房源
    def page_click_subway(self):
        self.base_click(page.app_subway)

    # 2、查找地铁线路五号线
    def page_click_channel(self, click_text):
        # 调用 从右到左滑动方法
        self.app_base_right_swipe_left(page.app_channel_area, click_text)

    # 3、查找房源
    def page_click_room(self, title):
        # 调用 从下向上滑动方法
        self.app_base_down_swipe_up(page.app_room_area, title)

    # 4、查找地铁线业务方法
    def page_app_rent(self, click_text, title):
        log.info("正在调用 查找房源信息业务方法 所属线路：{}， 标题：{}".format(click_text, title))
        self.page_click_subway()
        # 调用查找频道方法
        self.page_click_channel(click_text)
        # 调用 查找房源
        self.page_click_room(title)
