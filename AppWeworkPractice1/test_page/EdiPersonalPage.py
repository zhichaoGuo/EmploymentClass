from appium.webdriver.common.mobileby import MobileBy

from AppWeworkPractice1.test_page.BasePage import BasePage


class EdiPersonalPage(BasePage):
    def del_member(self):
        self.swipe_find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        from AppWeworkPractice1.test_page.ContactPage import ContactPage
        return ContactPage(self.driver)
