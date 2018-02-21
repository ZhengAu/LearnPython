# encoding=utf-8

# 递归函数的运用
# 注意：要有退出函数的标志，即结束标志


def test1(num):
    if num > 1:
        result = num + test1(num - 1)
    else:
        result = 1
    return result

num = int(input("Please input num: "))

result = test1(num)

print(result)
