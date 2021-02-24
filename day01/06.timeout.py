'''
1、上传文件的接口，上传1M的文件，上传2G的文件，耗时不一样，默认的超时时间不够用时，可以设置接口超时时间
2、接口性能测试，看借口是否能在某个时间内返回
'''
import requests

for i in range(10):
    try:
        r = requests.get("http://127.0.0.1:8080/carRental/car/addCar.action", timeout=0.05)  # 10ms
        print(r.text)
    except Exception as e:
        print(e)




