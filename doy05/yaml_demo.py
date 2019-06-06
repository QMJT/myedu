import yaml


if __name__ == '__main__':

    f = open('test.yaml',encoding='utf-8')
    y = yaml.load(f)
    print (y)