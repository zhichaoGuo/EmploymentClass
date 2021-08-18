from appium.webdriver.common import mobileby
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from AppWeworkPractice1.test_page.app import App


class TestAddmember:
    def test_addmember(self):
        faker = Faker('zh-CN')
        name = faker.name()
        phone = faker.phone_number()
        self.app = App()
        ele = self.app.start().go_to_main().go_contact_page().go_to_addmember().go_to_editmember().send_name(
            name).send_phone(phone).save().get_toast()

        assert ele.text == '添加成功'
