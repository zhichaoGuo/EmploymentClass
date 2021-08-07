import pytest
import yaml


from WebWeworkPractice1.test_page.main_page import MainPage


class TestDelmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.quit_page()

    def test_delmember(self):
        # 链式调用
        # 主页-通讯录-选择成员-删除
        self.main.goto_contact().click_member("任三").click_delmember()