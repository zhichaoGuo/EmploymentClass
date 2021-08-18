from appium.webdriver.common.mobileby import MobileBy

from AppWeworkPractice1.test_page.BasePage import BasePage


class PersonalPageMore(BasePage):
    def go_to_edipersonal(self):
        self.swipe_find(MobileBy.ID, "com.tencent.wework:id/b49").click()
        from AppWeworkPractice1.test_page.EdiPersonalPage import EdiPersonalPage
        return EdiPersonalPage(self.driver)
