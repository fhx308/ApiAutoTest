import pytest_check as check

def equal(real,expect,keys):
    '''
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['status'] == pass_data['expect']['status']
    assert r.json()['msg'] == pass_data['expect']['msg']
    简化为：
    Check.equal(r.json,fail_data["expect"],'code,status,msg')
    检查两个字典中，key对应的value是否一致
    不推荐直接判等r.json == fail_data["expect"]
    1、结果中有一些不关键信息，后面会有变化，会导致脚本不执行
    2、结果中有时间戳这类变化的信息，每次结果不同，需要变更数据
    3、结果可能很长，顺序发生变化，不方便维护
    :param real: 实际结果，字典格式
    :param expect: 预期结果，字典格式
    :param keys: 对比的key
    :return:
    '''
    ks = keys.split(",")  # 字符串在,处切割
    for k in ks:
        r = str(real.get(k))  # 根据k取value
        e = str(expect.get(k))  # 根据k取预期结果中的value，并转成字符串
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"检验{k}失败")
