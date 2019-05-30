dict1 ={'name':'qq','sex':'nan'}

dict2={'kchemg':'huaxue','lname':'zhangzhang'}



if __name__ == '__main__':
    print(dict1['name'])
    dict1.pop('sex')
    print(dict1)
    dict1['xuihao']='50'
    print(dict1)
    dict1['name']='fazi'
    print(dict1)

    dict.update(dict2)
    print(dict)
    d=dict(dict1,**dict2)
    print(d)
