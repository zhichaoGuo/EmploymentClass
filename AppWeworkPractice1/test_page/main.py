from appium.webdriver.webdriver import WebDriver

from AppWeworkPractice1.test_page.BasePage import BasePage
from AppWeworkPractice1.test_page.ContactPage import ContactPage


class MainPage(BasePage):
    def go_contact_page(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        return ContactPage(self.driver)
