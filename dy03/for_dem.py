def for_deng():
    for a in range(5):
        print('hello world')
        print(a)

def for_tt():
    for t in range(4,5):
        print('钱钱钱')
        print(t)

def for_tt1():
    for k in range(1,6,2):
        print(k)

def ban_list():
    a=[1,2,2,5,5,5,6,'85']
    for l in a:
        print(l)

    for o in range(len(a)):
        print(a[o])

def for_gg():
    for i in range(5):
        print('哈哈哈 小样')
        for j in range(2):
            print('我是嘻嘻嘻',end=';')
            print('\n')



def list_o():
    for  u in range(8):
        print(u)
        if u== 4:
            break

    for k in range(6):
        print(5)
        if u==6:
            continue


def low_bee():
    for q in range(1,10):
     for t in range(1,10):
         if q>=t:
             print('%s*%s=%s'%(q,t,q*t),end='')
    print('')







if __name__ == '__main__':
    # for_deng()
    # for_tt1()
    # ban_list()
    # for_gg()
    # list_o()
    low_bee()