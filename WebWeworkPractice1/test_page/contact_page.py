from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 通讯录页面
from WebWeworkPractice1.test_page.add_member_page import AddMember
from WebWeworkPractice1.test_page.base_page import BasePage


class Contact(BasePage):
    def click_add_member(self):
        sleep(1)
        while True:
            # *ele 解元组
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            # self.find_and_click(By.XPATH,"//*[@id='js_contacts78']/div/div[2]/div/div[2]/div[3]/div[1]/a[1]")
            ele_num = len(self.finds(By.ID, "username"))
            if ele_num > 0:
                break
        return AddMember(self.driver)

    def get_member(self):
        sleep(1)
        member_list = []
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in eles:
            member_list.append(value.get_attribute("title"))
        return member_list

    def click_member(self,member_name):
        self.find_and_click(By.XPATH,f"//*[@title='{member_name}']/../td[1]/input")
        return Contact(self.driver)

    def click_delmember(self):
        self.find_and_click(By.XPATH,"//*[@class='js_has_member']/div[1]/a[3]")
        return Contact(self.driver)