list = ['hhhjuu','意义借记卡','1235',123,15.5,5,2]

a = 'hello world'

#qiepianchaxun
def list_tt():
    print(list[-3])
    print(list[4:])
    print(type(list))
    print(list[1:4])

#  shangchu
def listt_():
    list.pop(-2)
    print(list)
    list.pop()
    print(list)

#xingzheng
def lisd_qq():
    lis=[123,'258',12.5,'就含糊见客户']
    lis.append('852')
    print(lis)
    lis.append(list)

    listu=[123,1474,'258']
    # list.append(listu)
#hebing
    lis.extend(listu)
    print(list)
    lis.extend(list)
#genggai
def list_update():
    update=[1,2,3,5,4,8]
    update[1]='25'
    print(update)
    update[2]=200
    print(update)


#paixu
def goder_by():
    qq=[8,7,6,9,7,3,2,]
    qq.sort()
    print(qq)
    qq.sort(reverse=True)
    print(qq)
    qq=set(qq)
    print(qq)
    # qq = list(set(qq))
    # print(qq)


def list_oo():
    kk=[12,147,258,258,963,'25']
    print(kk[1])
    print(kk[0:4])
    kk.pop(2)
    print(kk)
    kk.append(25)
    print(kk)
    kk.append('25')
    print(kk)
    kk[0]='5'
    print(kk)
    print(len(kk))




if __name__ == '__main__':
    # list_tt()
    # listt_()
    # lisd_qq()
    # list_update()
    # goder_by()
    list_oo()