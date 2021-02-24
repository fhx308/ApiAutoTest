'''
fixture级别：session、class、module、function(默认)
1、fixture为function(默认级别)，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例之后运行。
2、fixture为class级别的时候，如果一个class里面有多个用例，都调用了次fixture，
  那么此fixture只在此class里所有用例开始前执行一次。
3、fixture为module时，在当前.py脚本里面所有用例开始前只执行一次。
4、fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，
   如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里。

'''
import pytest

@pytest.fixture(scope='module')  # 模块级
def db():
    print("前置：连接数据库")
    yield
    print("后置，断开数据库连接")

@pytest.fixture(scope='module')
def login():
    print("前置，在首次调用login的地方执行前置")
    yield  # yield之前是前置，之后是后置
    print("后置：模块所有用例执行完执行后置")

def test_001():
    print("用例001")


def test_002(login,db):  # 这个用例前执行前置
    print("用例002")

def test_003(db,login):
    print("用例003")

def test_004():       # 这个用例后执行后置
    print("用例004")

