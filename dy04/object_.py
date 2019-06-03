class huam (object):
    def __init__(self,name,age,sex,gushi):
        self.name = name
        self.age = age
        self.sex =sex
        self.gushi =gushi

    def shijiao (self):
        print(self.name + '在睡觉' )


    def info (self):
        print('这个人叫%s,今年%s,他有个故事叫%s'%(self.name,self.age,self.gushi))

# class job (huam):
#     def __init__(self,name,age,sex,job):
#         # print(self.name+self.job)
#         print('姓名:%s%s')




if __name__ == '__main__':
    qui=huam('王大锤',50,'男','资深老师机')
    qui.info()
