# encoding=UTF-8
# 不定长参数
# (a,*b,**c) : a必须传递；b、c可传可不传，表示不定长的；b接受的是tuple，c接受的是dictionary
# c接受的是指定参数名的参数


def test1(a, *b):
    print(a)
    print(b)

test1(1, 2, 3, 4, 23, 23, 23, 45, 34, 99)

# 1
# (2,3,4,23,23,23,45,34,99)


def test2(a, *b, **c):
    print(a)
    print(b)
    print(c)

test2(1, 2, 3, 4, 5, m=6, n=7, x=8, y=9)

# 1
# (2, 3, 4, 5)
# {'m': 6, 'n': 7, 'x': 8, 'y': 9}
