import pytest
import yaml
from selenium import webdriver


class TestLogin:

    # @pytest.mark.skip
    def test_wechat(self):
        # chrome --remote-debugging-port=9222
        # 实例化浏览器设置
        opt = webdriver.ChromeOptions()
        # 设置浏览器设置的debugger地址
        opt.debugger_address = "127.0.0.1:9222"
        # 将设置好的浏览器设置传入driver中
        driver = webdriver.Chrome(options=opt)
        # 等待
        driver.implicitly_wait(10)
        driver.get('https://test-ccawtx0qdu3n.feishu.cn/messenger/?from=home_banner_login')
        # 获取页面cookies
        cookie = driver.get_cookies()
        print(cookie)
        # 将cookies保存为yaml格式文件
        with open("cookies.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)