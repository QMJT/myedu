import os


if __name__ == '__main__':
    pwd = os.getcwd()
    print(pwd)

    q=os.path.abspath('..')
    print(q)
    w=os.path.abspath('../../../../../')
    print(w)



