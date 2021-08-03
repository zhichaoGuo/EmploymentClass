"""
1、补全计算器（加法 除法）的测试用例

2、使用参数化完成测试用例的自动生成

3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：

使用等价类，边界值，因果图等设计测试用例

测试用例中添加断言，验证结果

灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""

import pytest
import yaml


class Calculator:
    def my_add(self, a, b):
        if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)):
            return a + b
        else:
            return "Err：001 输入类型错误"

    def my_division(self, a, b):
        if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)):

            if a == 0 and b != 0:
                return 0
            else:
                if a == 0 and b == 0:
                    return 'err:002 除数被除数都为零'
                else:
                    if a != 0 and b == 0:
                        return 'err:003 除数为零'
                    else:
                        return a / b

        else:
            return "Err：001 输入类型错误"


class TestCalculator(Calculator):
    def setup(self):
        print('开始计算')
        r = Calculator

    def teardown(self):
        print('计算结束')

    f = yaml.safe_load(open("TestCase.yaml", encoding='utf-8'))

    @pytest.mark.parametrize(['a', 'b', 'c'], f["add"])
    def test_my_add(self, a, b, c):
        r = Calculator
        print(a, b, c)
        assert r.my_add(self, a, b) == c

    @pytest.mark.parametrize("a,b,c", f["division"])
    def test_my_division(self, a, b, c):
        assert Calculator.my_division(self, a, b) == c
