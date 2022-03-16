import yaml
from selenium.webdriver.common.by import By

from FeiShu_Web_test.page.base_page import BasePage


class MainPage(BasePage):
    def go_to_contact_page(self):
        # 点击通讯录
        self.find_and_click(By.XPATH, '//*[@data-tip="tip-contacts"]')
        return self

    def add_user(self, name, mobile):
        # 只有在执行go_to_contact_page之后才可以执行
        # 点击添加团队成员
        self.find_and_click(By.XPATH, '//*[@class="larkc-btn larkc-btn-normal larkc-btn-info larkc-btn-large"]')
        # 点击用手机号添加
        self.find_and_click(By.XPATH, '//*[@id="__larkc-modall-container__"]/div[2]/div/div[2]/div/div/main/div[2]/div[1]/div[3]')
        # 向文本框输入手机号
        self.find_and_send(By.XPATH, '//*[@id="__larkc-modall-container__"]/div[2]/div/div[2]/div/div/main/div[2]/div[2]/form/div[1]/div/div/div[1]/div[1]/div[2]/input', mobile)
        # 向文本框输入姓名
        self.find_and_send(By.XPATH, '//*[@id="__larkc-modall-container__"]/div[2]/div/div[2]/div/div/main/div[2]/div[2]/form/div[1]/div/div/div[1]/div[2]/div/input', name)
        # 点击添加
        self.find_and_click(By.XPATH,'//*[@class="larkc-btn InviteMobileTab_button larkc-btn-normal larkc-btn-primary larkc-btn-large"]')

        return self

    def close_add_user_page(self):
        # 点击关闭按钮
        self.find_and_click(By.XPATH,'//*[@class="UnitedInvite_close"]')
        return self

    def go_to_messenger_page(self):
        # 返回聊天界面
        self.find_and_click(By.XPATH,'//*[@data-tip="tip-messenger"]')
        return self
