import requests

# 接口路径
url = "http://www.httpbin.org/post"
# 本地存在的文件
file = "d:/test.png"

with open(file, mode='rb') as f:
    cs = {"filename": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)


#上传图片(图片的接口)
url = 'http://127.0.0.1:8080/carRental/file/uploadFile.action'
file = "d:/test.png"
with open(file, mode='rb') as f:
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)

    uploadPath = r.json()['data']['src']
    print(uploadPath)



# 添加车
url = 'http://127.0.0.1:8080/carRental/car/addCar.action'
cs = {
     "carnumber": "甘H4567",
     "cartype": "轿车",
     "color": "白色",
     "carimg": uploadPath,
     "description": "空间大",
     "price": "250000",
     "rentprice": "3200",
     "deposit": "35000",
     "isrenting": "0"
}

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


