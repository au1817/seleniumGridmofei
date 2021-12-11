from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog
log = GetLog().get_logger()


# 新建类
class PageCenter(WebBase):
    # 点击手机号链接 进入后台
    def page_click_phonelink(self):
        self.base_click(page.del_phonelink)

    # 点击收藏房源
    def page_coll_room(self):
        self.base_click(page.del_coll_room)

    # 点击批量删除
    def page_all_del_link(self):
        self.base_click(page.del_all)

    # 点击选择框
    def page_all_check(self):
        # self.base_finds(page.del_allcheck)
        for el in self.base_finds(page.del_allcheck):
            el.click()

    # 点击删除图标进行批量删除
    def page_all_del_btn(self):
        self.base_click(page.del_btn)

    # 点击确定按钮
    def page_ok_btn(self):
        self.base_click(page.del_ok_btn)

    # 搜索暂无记录图片确认无收藏房源
    def page_search_picture(self):
        return self.base_get_attribute(page.del_no_exit)

    # 刷新窗口操作
    def page_refresh(self):
        self.web_base_refresh()

    # 组装批量删除业务方法
    def page_all_del(self):
        log.info("正在调用批量删除业务方法")
        # 判断是否有收藏房源
        # if self.page_search_picture() != page.del_src:
        self.page_click_phonelink()
        self.page_coll_room()
        self.page_all_del_link()
        self.page_all_check()
        self.page_all_del_btn()
        self.page_ok_btn()
        sleep(2)
        self.page_refresh()
        # else:
            # print("暂无收藏房源记录")
