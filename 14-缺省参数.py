# encoding=utf-8
# 缺省参数
# 注意：缺省的必须放在右边，放在左边则会报错

def test01(a,b):
    print(a)
    print(b)

def test02(a,b=100):
	print(a)
	print(b)

test01(100,200)

test02(100)
