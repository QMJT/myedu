class laimu(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


    def chifan (self):
        print('name'+'在网吧打LOL')

class tan (laimu):

    def chifan(self):




if __name__ == '__main__':
    get=laimu('天天',15,'男')
    get.chifan()
    tan()
