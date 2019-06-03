def jiujiu():
    for i in range(1,10):
        x=i+1
        for j in range(1,x):
           print('%s*%s=%s'%(j,i,j*i),end='    ')
        print('')


# 有一个篮子,里面有若干鸡蛋,
# 每次拿 4 个 最后剩一个,
# 每次拿五个剩四个,
# 每次拿6个 最后剩3个,
# 每次拿七个最后剩5个,
# 每次拿八个最后剩一个,
# 每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋


def jidan():
    for i in range(0,1000):
        if(i%4==1):
            if(i%5==4):
                if(i%6==3):
                    if(i%7==5):
                        if(i%8==1):
                            if(i%9==0):
                             print(i)

# 求1dao100数之间的偶数和

def oushu():
    he=0
    for i in range(1,100):
        h=i%2
        if h==0:
            he = he + i
    print(he)



#求两个数之间的偶数和


def sumoushu(a,b):







# 求1到50之间的奇数和
def jishu():
    sum = 0
    for i in range(1,51):
        k=i%2
        if k==1:
          sum=sum+i
    print(sum)




if __name__ == '__main__':
    # jiujiu()
    # jidan()
    # oushu()
    # jishu()
    oushu()