# encoding=utf-8
# 多继承
# 只能继承公有属性、公有方法


class Base(object):

    def test(self):
        print("------ test Base ------")


class A(Base):

    def test(self):
        print("------ test A ------")


class B(Base):

    def test(self):
        print("------ test B ------")

# 多继承的，用,隔开多个父类


class C(A, B):
    pass

c = C()
c.test()  # 若同名方法，父类中没有此方法，则会调用父类的父类的方法；都没有，则会报错


print(C.__mro__)
