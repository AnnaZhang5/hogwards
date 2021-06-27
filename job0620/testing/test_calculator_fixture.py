"""
__author__ = 'hogwarts19_zhl'
__time__ = '2021/3/19'
"""
import logging
import allure
import pytest
import yaml
from pythoncode.calculator import Calculator


# 获取加法的测试数据
def get_cal_adddata():
    with open('../datas/calculator.yml') as f:
        totals = yaml.safe_load(f)
        add_int_datas = totals['add']['int']['datas']
        add_int_ids = totals['add']['int']['ids']
        add_float_datas = totals['add']['float']['datas']
        add_float_ids = totals['add']['float']['ids']
    return add_int_datas, add_int_ids, add_float_datas, add_float_ids


# 获取除法的测试数据
def get_cal_divdata():
    with open('../datas/calculator.yml') as f:
        totals = yaml.safe_load(f)
        div_int_datas = totals['div']['int']['datas']
        div_int_ids = totals['div']['int']['ids']
        div_float_datas = totals['div']['float']['datas']
        div_float_ids = totals['div']['float']['ids']
    return div_int_datas, div_int_ids, div_float_datas, div_float_ids


# 通过fixture获取加法的整数数据，并参数化
@pytest.fixture(params=get_cal_adddata()[0], ids=get_cal_adddata()[1])
def get_int_data_fixture(request):
    return request.param


# 通过fixture获取加法的浮点数据，并参数化
@pytest.fixture(params=get_cal_adddata()[2], ids=get_cal_adddata()[3])
def get_float_data_fixture(request):
    return request.param


# 通过fixture获取除法的整数，并参数化
@pytest.fixture(params=get_cal_divdata()[0], ids=get_cal_divdata()[1])
def get_int_divdata_fixture(request):
    return request.param


# 通过fixture获取除法的浮点数据，并参数化
@pytest.fixture(params=get_cal_divdata()[2], ids=get_cal_divdata()[3])
def get_float_divdata_fixture(request):
    return request.param


@allure.feature('计数器')
class TestCalculator:
    # setup_class、teardown_class是在类执行前后分别执行一次
    # setup_method与teardown_method或setup与teardown在是每条用例执行前后执行一次
    @classmethod
    def setup_class(cls):
        logging.info("\n测试开始")
        cls.cal = Calculator()

    @classmethod
    def teardown_class(cls):
        logging.info("\n测试结束")

    def setup(self):
        logging.info("\n开始计算")

    def teardown(self):
        logging.info("\n结束计算")

    # @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (99, 0, 99)])
    '''
    此代码是使用parameterize进行参数化，对整数加法进行测试
    @pytest.mark.parametrize('a, b, expect', get_cal_adddata()[0], ids=get_cal_adddata()[1])
    def test_add_init(self, a, b, expect):
        assert expect == self.cal.add(a, b)
    '''
    '''
    以下代码使用自定义的fixture get_int_data_fixture进行参数化，
    get_data_fixture[0]为原来的a取值和ids别名1的值
    get_data_fixture[1]为原来的b取值和ids别名2的值
    get_data_fixture[2]为原来的expect的取值和ids别名3的值
    '''
    # 注allure.title中显示数据时，不要加f，不能写为f""
    @allure.title("整数相加_{get_int_data_fixture[0]}_{get_int_data_fixture[1]}")
    @allure.story("整数加法")
    def test_add_init(self, get_int_data_fixture):
        # 输出日记信息，记录本次使用的测试数据
        logging.info(f"test_add数据：{get_int_data_fixture}")
        allure.attach.file("../Image/测试截图1.jpg", name="测试截图", attachment_type=allure.attachment_type.JPG)
        assert get_int_data_fixture[2] == self.cal.add(get_int_data_fixture[0], get_int_data_fixture[1])

    '''
    此代码使用parameterize进行参数化，对浮点数加法进行测试
    @pytest.mark.parametrize('a, b, expect', get_cal_adddata()[2], ids=get_cal_adddata()[3])
    def test_add_float(self, a, b, expect):
        # 浮点数运算取2位小数，四舍五入
        assert expect == self.cal.add(a,b)
    '''
    # 使用fixture  get_float_data_fixture进行参数化，对浮点数加法进行测试
    @allure.story("浮点数加法")
    def test_add_float(self, get_float_data_fixture):
        # 浮点数运算取2位小数，四舍五入
        assert get_float_data_fixture[2] == self.cal.add(get_float_data_fixture[0], get_float_data_fixture[1])

    '''
    此代码使用parameterize进行参数化，对整数除法进行测试
    @pytest.mark.parametrize('a, b, expect', get_cal_divdata()[0], ids=get_cal_divdata()[1])
    def test_div_int(self, a, b, expect):
        assert expect == self.cal.div(a, b)
    '''
    # 使用自定义fixture  get_int_divdata_fixture进行参数化，对整数除法进行测试
    @allure.story("整数除法")
    def test_div_int(self, get_int_divdata_fixture):
        assert get_int_divdata_fixture[2] == self.cal.div(get_int_divdata_fixture[0], get_int_divdata_fixture[1])

    '''
    此代码使用parameterize进行参数化，对浮点数除法进行测试
    @pytest.mark.parametrize('a, b, expect', get_cal_divdata()[2], ids=get_cal_divdata()[3])
    def test_div_float(self, a, b, expect):
        assert expect == self.cal.div(a, b)    
    '''
    # 使用自定义fixture  get_float_divdata_fixture进行参数化，对浮点数除法进行测试
    @allure.story("浮点数法")
    def test_div_float(self, get_float_divdata_fixture):
        assert get_float_divdata_fixture[2] == self.cal.div(get_float_divdata_fixture[0], get_float_divdata_fixture[1])

    # 将除数是0的单独提取进行测试
    @allure.story("除法除数为零")
    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert 'zero' == self.cal.div(1, 0)


if __name__ == '__main__':
    pytest.main()
