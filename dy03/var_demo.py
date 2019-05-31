quan='你好啊'


def avr_qq():
    print(quan)


def avr_2():
    global quan
    quan='aaaaaa'
    print(quan)




if __name__ == '__main__':
    avr_qq()
    avr_2()
    avr_qq()