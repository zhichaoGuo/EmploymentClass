from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from WebWeworkPractice1.test_page.add_member_page import AddMember
from WebWeworkPractice1.test_page.base_page import BasePage
from WebWeworkPractice1.test_page.contact_page import Contact


# 主页


class MainPage(BasePage):
    # 主页URL
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击通讯录，跳转至通讯录
    def goto_contact(self):
        self.find_and_click(By.ID, "menu_contacts")
        return Contact(self.driver)

    # 点击添加成员，跳转至添加成员页面
    def click_add_member(self):
        sleep(1)
        # 循环等待添加成员按钮可点击后点击
        while True:
            # *ele 解元组
            self.find_and_click(By.LINK_TEXT, "添加成员")
            ele_num = len(self.finds(By.ID, "username"))
            if ele_num > 0:
                break
        return AddMember(self.driver)