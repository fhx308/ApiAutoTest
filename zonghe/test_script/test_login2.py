import pytest

from zonghe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param


def test_login(login_data):
    # 注册用户
    print("注册数据",login_data['data'])
    # 登录
    print("登录数据",login_data['logindata'])
    # 检查结果
    # 删除用户
    pass
