from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 添加成员信息
from WebWeworkPractice1.test_page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, name, id, phone):
        # 避免循环导入；局部导入
        from WebWeworkPractice1.test_page.contact_page import Contact

        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(id)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        sleep(5)
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")
        return Contact(self.driver)
