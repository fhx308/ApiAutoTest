'''
接口测试：
   使用requests中的get、post、方法调用接口，检查返回值是否正确
'''

#获取用户列表
import requests
url = 'http://192.168.150.222:8081/futureloan/mvc/api/member/list'
url = 'http://jy001:8081/futureloan/mvc/api/member/list'
#发送get请求
r = requests.get(url)
# 打印响应
print(r.text)

assert r.status_code == 200
assert r.reason == 'OK'
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'
assert rjson["msg"] == "获取用户列表成功"

print(r.headers)

##########################get请求，带参数####################################
# 注册接口，参数拼接在url后，？后面是参数
# url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=13321327859&pwd=123456"
# #发送get请求
# r = requests.get(url)
# print(r.text)
# rjson = r.json()
# assert rjson['status'] == 1
# assert rjson['code'] == '10001'

print('==========================+++++++++===========================')

#####注册接口，使用param传参
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {
    "mobilephone":"18894495130",
    "pwd":"159357",
    "regname":"request_test"
}
r = requests.get(url, params=cs)
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20110'
assert rjson["msg"] == "手机号码已被注册"

#查询手机号码归属地
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13321327857"
#url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
# cs = {
#     "tel":"18894495130"
# }
#r = requests.get(url, params=cs)
r = requests.get(url)
print(r.text)
#print(r.json()) # 报错，返回的结果不是json格式
assert "中国移动" in r.text


