def assert_qq():
    a='123'
    d='258'
    try:
        assert a in d
        assert a not in d
        assert '123'=='123'
    except:
        print('duanyanshibai')


def  assert_2():
    d='ni'
    f='lo'
    j=123
    try:
        assert d in f
        assert f in j
    except:
        print('断言失败')


def assert_l():
    q=123
    e=158
    try:
        assert q in e

    except:
        print('chenggong')





if __name__ == '__main__':
    # assert_qq()
    # assert_2()
    assert_l()
