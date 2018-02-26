# encoding=utf-8
# 类对象，既是类；实例对象
# 类属性，不在方法内的；实例属性，在方法内的
# 类方法，用@classmethod声明的；实例方法
# 定义实例对象时，类方法、实例方法和类属性都是在类的内存中的，不会在实例对象的内存中
'''
类对象，可以直接调用类属性，类方法
但不能调用实例属性，实例方法

实例对象，可以获取实例属性和类属性的值，但只能修改实例属性，不能修改类属性
可以调用实例方法和类方法
'''


class People(object):
    """docstring for People"""
    nation = '汉族'  # 类属性
    personNum = 0

    def __init__(self, name, age):  # 实例方法
        self.name = name  # 实例属性
        self.age = age
        # 可在此调用类方法
        self.setPersonNum()

    @classmethod
    def setNation(cls, nation):  # 类方法
        cls.nation = nation

    @classmethod
    def setPersonNum(cls):
        cls.personNum += 1

print(People.nation)
People.setNation('蒙古族')
print(People.nation)
print(People.personNum)
lily = People('lily', 22)
print(People.personNum)
kitty = People('kitty', 28)
print(People.personNum)
