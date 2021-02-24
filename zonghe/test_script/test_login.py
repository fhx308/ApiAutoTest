'''
测试登录
'''
import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MysqlOp

# 前置条件，注册的数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param

# 登录的测试数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param

# 测试前置语后置，环境准备与清理
@pytest.fixture()
def register(setup_data, baserequest, url, db_info):
    # 注册用户
    # 初始化环境
    MysqlOp.delete_user(db_info, setup_data['data']['mobilephone'])
    # 下发请求
    Member.register(baserequest, url, setup_data['data'])
    yield

    # 删除用户
    MysqlOp.delete_user(db_info, setup_data['data']['mobilephone'])

def test_login(db_info,login_data,baserequest,url):
    print(login_data)
    # 初始化环境
    MysqlOp.delete_user(db_info, login_data['data']['mobilephone'])
    # 下发登录请求
    r = Member.login(baserequest, url, login_data['data'])
    # 检查结果
    # 清理环境：删除用户
    MysqlOp.delete_user(db_info, login_data['data']['mobilephone'])








