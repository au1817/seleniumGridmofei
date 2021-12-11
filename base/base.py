from time import sleep
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog
log = GetLog.get_logger()


# 新建类
class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找：{}元素".format(loc))
        return (WebDriverWait(self.driver, timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 查找一组元素方法 封装
    def base_finds(self, loc, timeout=30, poll=0.5):
        log.info("正在查找一组：{}元素".format(loc))
        return (WebDriverWait(self.driver, timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_elements(*loc)))


    # 输入方法 封装
    def base_input(self, loc, value):
        # 1、找到元素
        el = self.base_find(loc)
        # 2、清空
        sleep(1)
        log.info("正在对：{}元素进行清空操作".format(loc))
        el.clear()
        # 3、输入内容
        log.info("正在对：{}元素 输入：{}内容操作".format(loc,value))
        el.send_keys(value)

    # 点击方法 封装
    def base_click(self, loc):
        sleep(1)
        log.info("正在对：{}元素进行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取元素文本方法 封装
    def base_get_text(self, loc):
        sleep(1)
        log.info("正在获取：{}元素的文本操作".format(loc))
        return self.base_find(loc).text

    # 获取元素属性方法 封装
    def base_get_attribute(self, loc, att):
        sleep(1)
        log.info("正在获取：{}元素的属性操作".format(loc))
        return self.base_find(loc).get_attribute(att)

    # 截图方法 封装
    def base_get_image(self):
        log.info("正在进行截图操作")
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入报告方法
        log.info("正在将图片写入报告")
        self.base_write_img()

    # 将图片写入报告方法 封装
    def base_write_img(self):
        with open("./image/err.png", "rb")as f:
            # 调用allure.attach方法将图片写入报告中
            allure.attach("错误原因", f.read(), attachment_type=allure.attachment_type.PNG)
