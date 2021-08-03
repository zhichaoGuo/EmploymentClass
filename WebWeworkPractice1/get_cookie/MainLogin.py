from time import sleep

import pytest
import yaml
from selenium import webdriver


class TestLogin:

    @pytest.mark.skip
    def test_wechat(self):
        # chrome --remote-debugging-port=9222 https://www.bilibili.com/
        # 实例化浏览器设置
        opt = webdriver.ChromeOptions()
        # 设置浏览器设置的debugger地址
        opt.debugger_address = "127.0.0.1:9222"
        # 将设置好的浏览器设置传入driver中
        driver = webdriver.Chrome(options=opt)
        # 等待
        driver.implicitly_wait(10)
        # 点击通讯录
        # driver.find_element_by_xpath("//*[@id=‘menu_contacts’]/span").click()
        driver.find_element_by_css_selector("#menu_contacts > span").click()
        # 获取页面cookies
        driver.find_element_by_xpath("//*[@title='任三']/../td[1]/input") .click()
        name="任三"
        print('title={name}')
        cookie = driver.get_cookies()
        # 将cookies保存为yaml格式文件
        with open("cookies.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    @pytest.mark.skip
    def test_login(self):
        # 设置浏览器
        driver = webdriver.Chrome()
        # 设置隐式等待
        driver.implicitly_wait(5)
        # 访问页面
        driver.get(
            "https://work.weixin.qq.com/wework_admin/loginpage_wx?redirect_uri=https://work.weixin.qq.com"
            "/wework_admin/frame#index")
        # 打开储存cookies的文件
        with open("cookies.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            # 传送cookies
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        # 带cookies访问网页
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)

    # @pytest.mark.skip
    def test_baiduwenku(self):
        # 设置浏览器
        driver = webdriver.Chrome()
        # 设置隐式等待
        driver.implicitly_wait(5)
        # 访问页面
        driver.get("https://wenku.baidu.com/")
        driver.find_element_by_xpath('//*[@id="app"]/div[11]/div/div[2]/i').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[2]/a').click()
        sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(1)