'''
fixtrue 嵌套
'''
import pytest
import random
import requests
# #生成用户名
# @pytest.fixture()
# def get_username():
#     return "admin" + str(random.randint(1,1000))
# 
# # 生成密码
# @pytest.fixture()
# def get_pwd():
#     return random.randint(100000,999999999)
# 
# @pytest.fixture()
# def get_login_data(get_username,get_pwd):
#     return {"username":get_username,"pwd":get_pwd}
# 
# # 测试用例
# def test_login(get_login_data):
#     print(f"测试登录，登录数据为：{get_login_data}")


# 练习 用fixture+request,优化注册接口

# 手机号为空
@pytest.fixture(params=[{"mobilephone": "", "pwd": ""},
                        {"mobilephone": "", "pwd": "123456"},
                        ])

def login_data2(request):  # 固定写法   request是pytest里的关键字，传request会从fixture里取数据
    return request.param  # 固定写法

# 手机号格式不正确
@pytest.fixture(params=[
                        {"mobilephone": "12345678910", "pwd": "123456"},
                        {"mobilephone": "1234567890", "pwd": "123456"},
                        {"mobilephone": "187932546500", "pwd": "123456"}])

def login_data3(request):
    return request.param

# 注册成功
@pytest.fixture(params=[
                        {"mobilephone": "18793254670", "pwd": "123456"}])

def login_data4(request):
    return request.param


# 密码不能为空
@pytest.fixture(params=[

    {"mobilephone": "18793254650", "pwd": ""}])

def login_data5(request):
    return request.param


#密码长度必须为6~18
@pytest.fixture(params=[
    {"mobilephone": "18793254650", "pwd": "12345"},
    {"mobilephone": "18793254653", "pwd": "1234561234561234567"}])
def login_data6(request):
    return request.param

#注册成功
@pytest.fixture(params=[

    {"mobilephone": "18793254666", "pwd": "123456"},
    {"mobilephone": "18793254667", "pwd": "1234567"},
    {"mobilephone": "18793254668", "pwd": "12345612345612345"},
    {"mobilephone": "18793254669", "pwd": "123456123456123456"}])
def login_data7(request):
    return request.param



def test_login2(login_data2):
    print(login_data2)  # 字典
    print(f"测试注册功能，使用手机号码：{login_data2['mobilephone']},密码：{login_data2['pwd']}，注册")

    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": login_data2['mobilephone'],
        "pwd": login_data2['pwd'],
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号不能为空" in r.text


# def test_login3(login_data3):
#     print(login_data3)  # 字典
#     print(f"测试注册功能，使用手机号码：{login_data3['mobilephone']},密码：{login_data3['pwd']}，注册")
#
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": login_data3['mobilephone'],
#         "pwd": login_data3['pwd'],
#     }
#     r = requests.post(url, data=cs)  # 路径
#     print(r.text)
#     assert "手机号码格式不正确" in r.text
#
# def test_login4(login_data4):
#     print(login_data4)  # 字典
#     print(f"测试注册功能，使用手机号码：{login_data4['mobilephone']},密码：{login_data4['pwd']}，注册")
#
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": login_data4['mobilephone'],
#         "pwd": login_data4['pwd'],
#     }
#     r = requests.post(url, data=cs)  # 路径
#     print(r.text)
#     assert "注册成功" in r.text
#
# def test_login5(login_data5):
#         print(login_data5)  # 字典
#         print(f"测试注册功能，使用手机号码：{login_data5['mobilephone']},密码：{login_data5['pwd']}，注册")
#
#         url = "http://jy001:8081/futureloan/mvc/api/member/register"
#         cs = {
#             "mobilephone": login_data5['mobilephone'],
#             "pwd": login_data5['pwd'],
#         }
#         r = requests.post(url, data=cs)  # 路径
#         print(r.text)
#         assert "密码不能为空" in r.text
#
#
# def test_login6(login_data6):
#     print(login_data5)  # 字典
#     print(f"测试注册功能，使用手机号码：{login_data6['mobilephone']},密码：{login_data6['pwd']}，注册")
#
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": login_data6['mobilephone'],
#         "pwd": login_data6['pwd'],
#     }
#     r = requests.post(url, data=cs)  # 路径
#     print(r.text)
#     assert "密码长度必须为6~18" in r.text
#
# def test_login7(login_data7):
#     print(login_data5)  # 字典
#     print(f"测试注册功能，使用手机号码：{login_data7['mobilephone']},密码：{login_data7['pwd']}，注册")
#
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": login_data7['mobilephone'],
#         "pwd": login_data7['pwd'],
#     }
#     r = requests.post(url, data=cs)  # 路径
#     print(r.text)
#     assert "注册成功" in r.text