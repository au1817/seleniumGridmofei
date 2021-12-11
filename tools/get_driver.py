from time import sleep

from selenium import webdriver
# 导包appium
import appium.webdriver

# 新建类
import page


class GetDriver:
    # 声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取driver
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 关闭driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver为空
        if cls.__app_driver is None:
            desired_caps = {
                            "platformName": "Android",              # 使用哪个移动操作系统平台
                            "platformVersion": '5.1',               # 移动操作系统版本
                            "deviceName": "192.168.153.102:5555",   # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
                            "appPackage": page.appPackage,          # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
                            "appActivity": page.appActivity,
                            }
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub",  desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断__app_driver不为空
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver().get_app_driver()
    sleep(8)
    GetDriver().quit_app_driver()
