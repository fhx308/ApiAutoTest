'''
session级别的前置和后置，放到conftest.py文件中
不需要import，pytest根据文件名字找到对应的方法
脚本层的一些公共方法，可以放到这里

一个工程可以包含多个conftest.py,conftest对同级文件以及该目录下的子目录生效

'''
import pytest

@pytest.fixture(scope='session')  #
def db():
    print("前置：连接数据库")
    yield
    print("后置，断开数据库连接")

@pytest.fixture(scope='session')
def login():
    print("前置，在首次调用login的地方执行前置")
    yield  # yield之前是前置，之后是后置
    print("后置：模块所有用例执行完执行后置")



