from appium.webdriver.common import mobileby
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from AppWeworkPractice1.test_page.BasePage import BasePage
from AppWeworkPractice1.test_page.EdimemberPage import EdimemberPage


class AddmemberPage(BasePage):
    def go_to_editmember(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return EdimemberPage(self.driver)

    def get_toast(self):
        # 建立toast的locator
        ele = (mobileby.MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        # 等待toast出现18956531761
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(ele))
        ele1 = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        return ele1
