"""
__author__ = 'hogwarts19_zhl'
__time__ = '2021/3/19'
"""
import logging
import pytest as pytest
import yaml
from pythoncode.calculator import Calculator


# 获取加法的测试数据
def get_cal_adddata():
    with open('../datas/calculator_add.yml') as f:
        totals = yaml.safe_load(f)
    return totals['datas'], totals['ids']


# 获取除法的测试数据
def get_cal_divdata():
    with open('../datas/calculator_div.yml') as f:
        totals = yaml.safe_load(f)
    return totals['datas'], totals['ids']


class TestCalculator:
    # setup_class、teardown_class是在类执行前后分别执行一次
    # setup_method与teardown_method或setup与teardown在是每条用例执行前后执行一次
    @classmethod
    def setup_class(cls):
        print("\n测试开始")
        cls.cal = Calculator()

    @classmethod
    def teardown_class(cls):
        print("\n测试结束")

    def setup(self):
        print("\n开始计算")

    def teardown(self):
        print("\n计算结束")

#    @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (99, 0, 99)])
    @pytest.mark.parametrize('a, b, expect', get_cal_adddata()[0], ids=get_cal_adddata()[1])
    def test_add_case(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize('a, b, expect', get_cal_divdata()[0], ids=get_cal_divdata()[1])
    def test_div_case(self, a, b, expect):
        assert expect == self.cal.div(a, b)

