import requests

#表单格式的数据：content—type：www-x-form-urlencoded,使用data传参
# 登录接口
# url = 'http://jy001:8081/futureloan/mvc/api/member/login'
# cs = {
#     "mobilephone":"13897845678",
#     "pwd":"123456"
# }
# r = requests.post(url, data=cs)
# print(r.text)
# #{"status":1,"code":"10001","data":null,"msg":"登录成功"}
# rjson = r.json()
# assert rjson['status'] == 1
# assert rjson['code'] == '10001'
# assert rjson["msg"] == "登录成功"
#
#
# # json格式的数据：content-type:application/json,使用json传参
# # 具体使用data还是就送传参，要看接口是怎么定义的
# #httpbin.org  是一个测试网站，不管发送什么数据，这个接口将发送的请求，封装成json格式的返回
# url = 'http://www.httpbin.org/post'
# cs = {
#     "mobilephone":"13897845678",
#     "pwd":"123456"
# }
# r = requests.post(url, data=cs)
# print("data传参", r.text)
# r = requests.post(url, json=cs)
# print("json传参", r.text)


# 租车系统，添加车辆
url = 'http://127.0.0.1:8080/carRental/car/addCar.action'
cs = {
     "carnumber": "甘N77777",
     "cartype": "轿车",
     "color": "白色",
     "carimg": "",
     "description": "空间大",
     "price": "250000",
     "rentprice": "3200",
     "deposit": "35000",
     "isrenting": "0"
}
'''
使用脚本添加的车辆。中文字符乱码，但使用界面添加的车辆，不会乱码
设置 charset=UTF-8 
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
就不会乱码了
'''


head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888" #https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=head, proxies=proxy)
print(r.text)
rjson = r.json()



