'''
操作mysql数据库的方法
'''
# 连接数据库
import pymysql

def connect(db_info):
    '''

    :param db_info:
    :return:
    '''

    user = db_info['user']
    pwd = db_info['pwd']
    host = db_info['host']
    database = db_info['name']
    port = db_info['port']
    try:
        conn = pymysql.connect(user=user,
        password=pwd,
        host=host,
        database=database,
        port=port,
        charset="utf8")
        print("数据库连接成功")

        return conn
    except Exception as e:
        print(f"连接数据库失败，异常信息为:{e}")


# 断开连接
def disconnect(conn):
    '''
    断开连接
    :param conn:
    :return:
    '''
    try:
        conn.close()
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为：{e}")


# 执行sql语句
def execute(conn, sql):
    try:
        cursor = conn.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        conn.commit()  # 提交
        cursor.close()  # 关闭游标
        print("执行sql语句成功")
    except Exception as e:
        print(f"执行sql语句失败，异常信息为:{e}")

def delete_user(db_info, mobilephone):
    '''
    根据手机号删除用户
    :param db_info:
    :param mobilephone:
    :return:
    '''
    conn = connect(db_info)
    execute(conn, f"delete from member where mobilephone={mobilephone};")
    disconnect(conn)


if __name__ == '__main__':
    # db_info = read_ini(r"test_env\env.ini", "db_info")
    # connect(eval(db_info))
    db_info = {"host":"192.168.1.64", "port": 3306, "name":"apple", "user":"root", "pwd":"123456"}
    #connect(db_info)

    delete_user(db_info, "18894495130")
