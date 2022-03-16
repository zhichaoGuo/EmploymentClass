from appium import webdriver

from FeiShu_App_test.page.base_page import BasePage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "Android",
                "platformVersion": "8.1.0",
                "deviceName": "16th",
                "appPackage": "com.ss.android.lark",
                "appActivity": ".main.app.MainActivity",
                "unicodeKeyBoard": True,
                "resetKeyBoard": True,
                "noReset": True
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(5)
            print("初始化desier_cap")
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        pass

    def find_and_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def find_and_send_key(self, by, locator, send_key):
        self.driver.find_element(by, locator).send_keys(send_key)
