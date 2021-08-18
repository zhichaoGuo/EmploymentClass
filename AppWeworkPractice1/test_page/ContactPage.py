from appium.webdriver.common.mobileby import MobileBy

from AppWeworkPractice1.test_page.AddmemberPage import AddmemberPage
from AppWeworkPractice1.test_page.BasePage import BasePage


class ContactPage(BasePage):
    def go_to_addmember(self):
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.swipe_find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddmemberPage(self.driver)

    def click_person(self, name):
        self.swipe_find(MobileBy.XPATH, f"//*[@text='{name}']").click()
        from AppWeworkPractice1.test_page.PersonalPage import PersonalPage
        return PersonalPage(self.driver)


