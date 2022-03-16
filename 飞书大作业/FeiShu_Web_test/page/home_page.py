from selenium.webdriver.common.by import By

from FeiShu_Web_test.page.base_page import BasePage
from FeiShu_Web_test.page.main_page import MainPage


class HomePage(BasePage):
    _base_url = 'https://www.feishu.cn/'

    # 由于采用复用浏览器的模式，所以本页面不再使用
    def go_to_work_page(self):
        # 点击免费使用
        self.find_and_click(By.XPATH, '//*[@class="heraComp_button heraComp_font-gilroy heraComp_button-large"]')
        # 跳转至工作页面（需要登录）
        return MainPage(self.driver)
