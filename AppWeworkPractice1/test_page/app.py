from appium import webdriver

from AppWeworkPractice1.test_page.BasePage import BasePage
from AppWeworkPractice1.test_page.main import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "android",
                # 模拟器
                # "devicename": "127.0.0.1:7555",
                # 真机
                "devicename": "192.168.101.9: 5555",
                "platformVersion": '8.1.0',
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "automationName": "uiautomator1",
                "unicodeKeyBoard": True,
                "resetKeyBoard": True,
                "noReset": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(5)
            print("初始化desier_cap")
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        pass

    def go_to_main(self):
        return MainPage(self.driver)
