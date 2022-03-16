from appium.webdriver.webdriver import WebDriver


def isElementPresent(driver, by, value):
    '''
    判断元素是否被展示
    :param driver: 传入driver
    :param by: 定位方式
    :param value: 定位值
    :return: 若被展示则返回Ture，若未被展示打印NoSuchElementException异常，并返回False
    '''
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        # 打印异常信息
        print(e)
        # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def swipe_find(self, aim_by, aim_locator, end_by=None, end_locator=None):
        '''
        在页面中滑动查找元素
        :param aim_by: 目标元素定位方式
        :param aim_locator: 目标元素定位值
        :param end_by: 终点元素定位方式，可不填写，进入死循环
        :param end_locator: 终点元素定位值，可不填写，进入死循环
        :return: 目标元素出现则返回目标元素，目标元素未出现则返回False
        '''
        # 如果没有输入终点元素则进入死循环查找目标元素
        if end_by is None:
            # 本死循环可加入循环次数改为For循环，到达循环次数还未找到则返回False
            num = 4
            for cycle in range(num):
                # while True:
                try:
                    # 查找目标元素
                    ele = self.driver.find_element(aim_by, aim_locator)
                except:
                    # 如果查找不到目标元素就进行滑动
                    size = self.driver.get_window_size()
                    width = size.get('width')
                    height = size.get('height')
                    start_x = width / 2
                    start_y = height * 0.8
                    end_x = start_x
                    end_y = height * 0.2
                    duration = 2000
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)
                else:
                    # 返回目标元素
                    return ele
                if cycle == num - 1:
                    return False

        # 如果输入了终点元素
        else:
            # 判断终点元素是否已经出现
            if isElementPresent(driver=self.driver, by=end_by, value=end_locator):
                # 终点元素已经出现
                try:
                    # 查找目标元素
                    ele = self.driver.find_element(aim_by, aim_locator)
                except:
                    # 差找不到返回False
                    return False
                else:
                    # 查找到了返回目标元素
                    return ele
            # 重点元素还未出现
            else:
                # 循环到终点元素出现为止
                while not isElementPresent(driver=self.driver, by=end_by, value=end_locator):
                    size = self.driver.get_window_size()
                    width = size.get('width')
                    height = size.get('height')
                    start_x = width / 2
                    start_y = height * 0.8
                    end_x = start_x
                    end_y = height * 0.2
                    duration = 2000
                    # 查找目标元素
                    try:
                        ele = self.driver.find_element(aim_by, aim_locator)
                        print("进入try")
                    # 目标元素未出现则滑动
                    except:
                        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
                        print("进入滑动")
                    # 目标元素出现则返回目标元素
                    else:
                        print("进入return")
                        return ele
                # 滑动到终点元素出现
                else:
                    # 查找目标元素
                    try:
                        ele = self.driver.find_element(aim_by, aim_locator)
                    # 目标元素未出现则返回False
                    except:
                        return False
                    # 目标元素出现则返回目标元素
                    else:
                        return ele