'''
Mock:  1、接口测试时，场景不好构造出来，用Mock模拟某个场景的返回值
       2、依赖第三方接口或其他项目的接口，单所以来的接口还未开发完成，自己的已开发完成
          该怎样测试
'''
from unittest import mock
import requests
import pytest



# # 接口地址:http://www.zhifu.com/pay
# # 方法：post
# # 参数：{“订单号”：1232,"支付金额"：123,"支付方式"：“余额宝”}
# # 返回值是json格式{“code”:10001,"msg"：“支付成功”}
# # 返回值是json格式{“code”:10002,"msg"：“支付失败”}
# def zhifu(data):
#     r = requests.post("http://www.zhifu.com/pay", data)
#     return r.json()
#
# def test_zhifu():
#     data = {"订单号":1232,"支付金额":123,"支付方式":"余额宝"}
#     # return_value是参数
#     zhifu = mock.Mock(return_value={"code":10002,"msg":"支付成功"})
#     r = zhifu(data)
#     assert r['msg'] == "支付成功"
#
#
# # 模块名.方法名
# # 模块名.类名.方法名
# @mock.patch("test_012.zhifu",return_value={"code":10002,"msg":"支付成功"})
# def test_zhifu2(aa):  # 这里要传一个参数，虽然参数在内部没有用到
#     data = {"订单号": 1232, "支付金额": 123, "支付方式": "余额宝"}
#     r = zhifu(data)
#     assert r['msg'] == "支付成功"

# http://jy001:8081/futureloan/mvc/api/member/register

# 注册
@pytest.fixture(params=[{"mobilephone":"18894495133","pwd":"123456"}])
def register(request):
    return request.param

# 登录

@pytest.fixture(scope='function',params=[{"mobilephone":"18894495133","pwd":"123456"}])  # 默认是function级别的。
def login(request):
    return request.param

# 充值
@pytest.fixture(params=[{"mobilephone":"18894495133","amount":"1000"}])  # 默认是function级别的。
def amount(request):
    return request.param




# 注册成功
def test_register(register):
    print(register)  # 字典
    print(f"测试注册功能，使用手机号码：{register['mobilephone']},密码：{register['pwd']}，注册")

    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": register['mobilephone'],
        "pwd": register['pwd'],
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text

# 登录
def test_login(login):
    print(login)  # 字典
    print(f"测试注册功能，使用手机号码：{login['mobilephone']},密码：{login['pwd']}，注册")

    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": login['mobilephone'],
        "pwd": login['pwd'],
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "登录成功" in r.text


# 充值
def test_amount(amount):
    print(amount)  # 字典
    print(f"测试注册功能，使用手机号码：{amount['mobilephone']},密码：{amount['amount']}，注册")

    url = "http://jy001:8081/futureloan/mvc/api/member/recharge"
    cs = {
        "mobilephone": amount['mobilephone'],
        "amount": amount['amount'],
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "成功" in r.text

# 取现
def test_amount(amount):
    print(amount)  # 字典
    print(f"测试注册功能，使用手机号码：{amount['mobilephone']},密码：{amount['amount']}，注册")

    url = "http://jy001:8081/futureloan/mvc/api/member/withdraw"
    cs = {
        "mobilephone": amount['mobilephone'],
        "amount": amount['amount'],
    }
    r = requests.post(url, data=cs)  # 路径

    quxian = mock.Mock(return_value={"msg": "成功"})
    a = quxian()
    assert "成功" in a['msg']


