from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from get_cookie.MainLogin import TestLogin


class BasePage:
    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        print("in base page run init")
        if _driver_base is None:
            # # 避免driver重复初始化，第一次初始化的时候driver是空的，就进行初始化
            # opt = webdriver.ChromeOptions()
            # # 设置debug地址
            # opt.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=opt)

            # 设置浏览器
            self.driver = webdriver.Chrome()
            # 设置隐式等待
            self.driver.implicitly_wait(5)
            # 访问页面
            self.driver.get(
                "https://work.weixin.qq.com/wework_admin/loginpage_wx?redirect_uri=https://work.weixin.qq.com"
                "/wework_admin/frame#index")
            # 打开储存cookies的文件
            import yaml

            with open("../../get_cookie/cookies.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                # 传送cookies
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            # 带cookies访问网页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

            self.driver.implicitly_wait(10)
        else:
            self.driver = _driver_base

        # if self._base_url != "":
        #     self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        ele: WebElement = self.find(by, locator)
        ele.click()
        return ele

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def quit_page(self):
        self.driver.quit()