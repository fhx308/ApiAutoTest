'''
更灵活的一种测试前置和后置：fixture
  可以不用setup、teardown
  使用起来灵活

'''
import pytest

# 测试前置：初始化的东西放在前置，环境初始化，测试数据准备
# 测试完清理的步骤方法放在后置里面


@pytest.fixture(scope='function')  # 默认是function级别的。
def login():
    print("登录系统")
    yield  # yield之前是前置，之后是后置
    print("退出系统")
    print("测试结束")



def test_query():
    print("查询功能，不需要登录")

def test_add(login):
    print("添加功能，需要登录")

@pytest.mark.usefixtures('login')
def test_delete():
    print("删除功能，需要登录")

def test_register():
    print("注册功能，不需要登录")