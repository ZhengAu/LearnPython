# encoding=utf-8
# 全局变量
# 若要在函数内改变全局变量的值，需要在修改前用global声明

num = 100


def changeNum():
    global num
    print(num)
    num += 100
    print(num)


changeNum()
