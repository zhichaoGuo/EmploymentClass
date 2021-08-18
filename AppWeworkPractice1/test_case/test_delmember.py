from appium.webdriver.common.mobileby import MobileBy

from AppWeworkPractice1.test_page.app import App


class TestDelmember:
    def test_delmember(self):
        del_name = "张十二"
        self.app = App()
        ele = self.app.start().go_to_main().go_contact_page().click_person(
            del_name).go_to_personalpage_more().go_to_edipersonal().del_member().swipe_find(MobileBy.XPATH,
                                                                                                f"//*[@text={del_name}]",
                                                                                                MobileBy.XPATH,
                                                                                                "//*[@text='添加成员']")
        assert ele is False
