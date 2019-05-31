
def jiujiu():
    for i in range(1,10):
        x=i+1
        for j in range(1,x):
            print('%s*%s=%s'%(j,i,j*i),end='   ')
        print('')

def



def open_qq1():
    qwe=open('aser.txt',"a+")
    for i in range(5):
        qwe.write('hello world\n')


def open_qq3():

    qwe=open('aser.log','w+')
    for i in range(6):
        qwe.write('天龙八部步,啦啦啦啦啦啦拉拉拉拉啦\n')


def open_qq2():
    qwe = open('aser.txt', "r")
    print(qwe.readlines())



def pen_gaga():
    qwe = open('aser.txt', "r")
    print(qwe.readline())



if __name__ == '__main__':
    # pen_gaga()
    # open_qq3()
    jiujiu()
