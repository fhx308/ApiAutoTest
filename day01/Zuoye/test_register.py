import requests

def test_register_001():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "",
        "pwd": "",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号不能为空" in r.text

def test_register_002():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号不能为空" in r.text

def test_register_003():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "12345678910",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号码格式不正确" in r.text

def test_register_004():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "1234567890",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号码格式不正确" in r.text

def test_register_005():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "187932546500",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "手机号码格式不正确" in r.text

def test_register_006():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254650",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text


def test_register_007():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254650",
        "pwd": "",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "密码不能为空" in r.text

def test_register_008():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254650",
        "pwd": "12345",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "密码长度必须为6~18" in r.text


def test_register_009():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254650",
        "pwd": "123456",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text


def test_register_0010():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254651",
        "pwd": "1234567",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text


def test_register_0011():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254652",
        "pwd": "1234561234561234567",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text

def test_register_0012():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254652",
        "pwd": "12345612345612345678",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "注册成功" in r.text

def test_register_0013():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {
        "mobilephone": "18793254653",
        "pwd": "123456123456123456781",
    }
    r = requests.post(url, data=cs)  # 路径
    print(r.text)
    assert "密码长度必须为6~18" in r.text




