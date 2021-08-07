from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from WebWeworkPractice1.test_page.add_member_page import AddMember
from WebWeworkPractice1.test_page.base_page import BasePage
from WebWeworkPractice1.test_page.contact_page import Contact


# 主页


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self.find_and_click(By.ID, "menu_contacts")
        return Contact(self.driver)

    def click_add_member(self):
        sleep(1)
        while True:
            # *ele 解元组
            self.find_and_click(By.LINK_TEXT, "添加成员")
            # self.find_and_click(By.XPATH,"//*[@id='js_contacts78']/div/div[2]/div/div[2]/div[3]/div[1]/a[1]")
            ele_num = len(self.finds(By.ID, "username"))
            print("in contact page run while")
            if ele_num > 0:
                break
        print("in contact page run click add member")
        return AddMember(self.driver)