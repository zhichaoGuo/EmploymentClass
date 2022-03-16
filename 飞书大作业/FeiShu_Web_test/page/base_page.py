import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        print("in base page run init")
        if _driver_base is None:
            # 避免driver重复初始化，第一次初始化的时候driver是空的，就进行初始化
            # 复用浏览器
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            # 设置隐式等待
            self.driver.implicitly_wait(5)

            # 由于选择使用复用浏览器的模式执行用例，所以以下代码注释掉了。
            # # 设置浏览器
            # self.driver = webdriver.Chrome()
            # # 设置隐式等待
            # self.driver.implicitly_wait(5)
            # # 访问页面
            # self.driver.get("https://www.feishu.cn/")
            # self.driver.maximize_window()

        else:
            self.driver = _driver_base

    def find_and_click(self, by, locator):
        ele: WebElement = self.find(by, locator)
        ele.click()
        return ele

    def find_and_send(self, by, locator, send_key):
        ele: WebElement = self.find(by, locator)
        ele.send_keys(send_key)
        return ele

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def quit_page(self):
        self.driver.quit()
