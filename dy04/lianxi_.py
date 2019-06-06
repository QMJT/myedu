class laimu(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


    def chifan (self):
        print(self.name+'在网吧打LOL')

class tan (laimu):

    def __init__(self,name,age,sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job =job

    def dadsa(self):
        print(self.name+'在打游戏')




if __name__ == '__main__':
    # get=laimu('天天',15,'男')
    # get.chifan()
    # tan()

    qq=tan('染发膏','14','个','员工')

    qq.dadsa()
