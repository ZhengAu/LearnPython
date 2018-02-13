# encoding=UTF-8
# 逗号隔开，直接返回多个值，类似a,b=100,200
# 返回列表
# 返回元组
# 返回字典


def fn(num1, num2):
    return num1 + num2, num1 ** num2

x, y = fn(100, 2)

print("和：", x, "\n幂：", y)
