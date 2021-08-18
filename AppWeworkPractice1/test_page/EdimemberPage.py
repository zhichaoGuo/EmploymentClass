from AppWeworkPractice1.test_page.BasePage import BasePage


class EdimemberPage(BasePage):
    def send_name(self, name):
        # 输入姓名
        self.driver.find_element_by_id("com.tencent.wework:id/ays").send_keys(name)
        return self

    def send_phone(self, phone):
        # 输入手机号
        self.driver.find_element_by_id("com.tencent.wework:id/f4m").send_keys(phone)
        return self

    def save(self):
        # 点击添加
        from AppWeworkPractice1.test_page.AddmemberPage import AddmemberPage
        self.driver.find_element_by_id("com.tencent.wework:id/ac9").click()

        return AddmemberPage(self.driver)
