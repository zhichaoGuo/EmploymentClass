import pytest
import yaml

from test_page import contact_page
from test_page.main_page import MainPage
from selenium import webdriver
import test_page.contact_page


class TestDelmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.quit_page()

    def test_delmember(self):
        # 链式调用
        # 主页-通讯录-选择成员-删除
        self.main.goto_contact().click_member("任三").click_delmember()