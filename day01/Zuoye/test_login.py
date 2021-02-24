import requests

def test_login_001():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": "",
        "pwd": "",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号不能为空" in r.text

def test_login_002():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": "18793254651",
        "pwd": "",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "密码不能为空" in r.text

def test_login_003():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": "18793254651",
        "pwd": "459623",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "用户名或密码错误" in r.text

def test_login_004():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": "18793254690",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "用户名或密码错误" in r.text

def test_login_005():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs = {
        "mobilephone": "15809466321",
        "pwd": "123456"
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    # rjson = r.json()
    # assert rjson["msg"] == "登录成功"
    assert "登录成功" in r.text