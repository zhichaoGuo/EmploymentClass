import os
from time import sleep

import pytest
import yaml
from selenium import webdriver

from FeiShu_Web_test.page.home_page import HomePage
from FeiShu_Web_test.page.main_page import MainPage


class TestContactMemberWeb:
    '''
    因为使用的复用浏览器所以需要先在命令行中输入以下命令
    chrome --remote-debugging-port=9222 https://test-ccawtx0qdu3n.feishu.cn/messenger/?from=home_banner_login
    '''
    def setup(self):
        # 在不开启浏览器的情况下复用浏览器
        # cmd_chrome='chrome --remote-debugging-port=9222 https://test-ccawtx0qdu3n.feishu.cn/messenger/?from=home_banner_login'
        # os.system(cmd_chrome)
        self.main = MainPage()

    def teardown(self):
        # 退出浏览器
        self.main.quit_page()

    def test_add_user(self):
        # 执行添加用户的操作，并回到message界面
        self.main.go_to_contact_page().add_user('郭志', '15076166089').close_add_user_page().go_to_messenger_page()
        sleep(3)

    @pytest.mark.skip
    def test_cookies(self):
        # 测试传cookies，发现失败，所以采用复用浏览器的方式
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://test-ccawtx0qdu3n.feishu.cn/messenger/?from=home_banner_login")
        with open("cookies.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            # 传送cookies
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://test-ccawtx0qdu3n.feishu.cn/messenger/?from=home_banner_login")
