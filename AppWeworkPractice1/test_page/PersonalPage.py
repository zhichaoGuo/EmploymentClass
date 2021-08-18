from appium.webdriver.common.mobileby import MobileBy

from AppWeworkPractice1.test_page.BasePage import BasePage


class PersonalPage(BasePage):
    def go_to_personalpage_more(self):
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/h8g').click()
        from AppWeworkPractice1.test_page.PersonalPageMore import PersonalPageMore
        return PersonalPageMore(self.driver)
