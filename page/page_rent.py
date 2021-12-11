from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog
log = GetLog().get_logger()


class PageRent(WebBase):
    # 点击我要租房
    def page_click_rent_link(self):
        self.base_click(page.rent_link)

    # 输入搜索内容
    def page_input_info(self, values):
        self.base_input(page.rent_search, values)

    # 点击搜索按钮
    def page_input_btn(self):
        self.base_click(page.rent_search_btn)

    # 筛选点击朝向不限 点击选择南
    def page_more_choice(self):
        self.web_base_click_element(page.rent_direction, page.rent_direction_text)

    # 点击房源列表第一个进入详情页
    def page_click_rents(self):
        self.base_click(page.rent_info)

    # 点击收藏按钮
    def page_click_collection(self):
        self.base_click(page.rent_collection)
        sleep(1)
        # result = self.base_get_text(page.rent_collection_result)
        # print("获取的文本为：", result)
        # return result

    # 在新增窗口进行操作
    def page_new_window(self):
        # 获取当前主窗口句柄
        hd = self.driver.current_window_handle
        # 点击链接，启动另一个窗口
        self.page_click_rents()
        # 获取由当前driver启动的所有句柄
        hds = self.driver.window_handles
        # 遍历所有窗口句柄
        for h in hds:
            # 判断遍历的句柄不等于当前主窗口句柄
            if h != hd:
                # 切换窗口
                self.driver.switch_to.window(h)
                sleep(1)
                att = self.base_get_attribute(page.rent_collection, att="class")
                self.page_click_collection()
                try:
                    if att == self.base_get_attribute(page.rent_collection, att="class"):
                        log.error("收藏成功！")
                        print("收藏成功！")
                except Exception as e:
                    log.error("收藏不成功！错误原因：{}".format(e))
                    print("收藏不成功！")
                finally:
                    print("")
                self.driver.close()
        self.driver.switch_to.window(hd)

    # 组装租房业务方法
    def page_rent(self, values):
        self.page_click_rent_link()
        self.page_input_info(values)
        self.page_input_btn()
        self.page_more_choice()
        self.page_new_window()


