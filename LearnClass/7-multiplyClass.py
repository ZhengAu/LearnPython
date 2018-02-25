# encoding=utf-8
# 多继承
# 只能继承公有属性、公有方法


class A(object):

    def test(self):
        print("------ test A ------")

    def testA(self):
        print("------ test A ------")


class B(object):

    def test(self):
        print("------ test B ------")

    def testB(self):
        print("------ test B ------")

# 多继承的，用,隔开多个父类


class C(A, B):
    pass

c = C()
c.test()  # 若同名方法，只会调用第一个继承的类的方法
c.testA()
c.testB()
