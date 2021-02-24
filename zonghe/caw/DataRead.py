'''
读取数据的文件
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取工程路径
    :return: F:\PyCharm Community Edition 2020.1\jbr\bin\ApiAutoTest\zonghe
    '''
    # 当前文件路径
    file_path = os.path.realpath(__file__)
    #print("当前文件路径", file_path)
    # 当前文件所在目录
    dir_path = os.path.dirname(file_path)
    #print("当前文件所在目录", dir_path)
    # 再上一级目录
    dir_path = os.path.dirname(dir_path)
    # 最后拼个“\”
    return dir_path + "\\"

def read_ini(file_path, key):
    '''
    读取配置文件
    :param file_path: 配置文件路径
    :param key: 配置文件中的key，比如url
    :return: 返回key对应的value
    '''


    # python内置的模块configparser
    config = configparser.ConfigParser()
    file_path = get_project_path() + file_path
    config.read(file_path)
    value = config.get("env", key)
    return value

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding='utf-8') as f:
        file_content = f.read()
        # 用yaml中的load方法，将文件转成yaml格式的
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content  # 列表嵌套字典


if __name__ == '__main__':
    v = read_ini(r"\test_env\env.ini", "url")
    print(v)
    print("================+++++=================")
    v = read_ini(r"\test_env\env.ini", "db_info")
    print(v)
    content = read_yaml("test_data/register_fail.yaml")
    print(content)
