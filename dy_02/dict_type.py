import json


wdict={'username':'admin',"password":"123456",'sex':'nv'}
#字典是以花括号{}包起来的  :  前面是key 后面是 velue


def dictt():
    print(dict['username'])
    print(dict["password"])

def dict_update():
    dict['username']='qmjt'
    print(dict)

def pop_dict():
    dict.pop('username')
    print(dict)


def adict ():
    ddict={'sex':'nan','get':'25'}

    as=(2,'25')
    wdict.update(ddict)
    print(wdict)


    we=dict(wdict,**ddict)
    print(we)

















if __name__ == '__main__':
    # dictt()
    # dict_update()
    # pop_dict()
    adict()