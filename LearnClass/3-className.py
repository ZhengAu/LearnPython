# encoding=UTF-8

# 如果有(object)：新式类
# 没有的，则为经典类

# 在类中的属性前加上 __ 是私有属性，不能顺便更改
# 可通过类中设置的函数，来进行更改

class Person:

    def __init__(self, name, age):
        # 在属性前面加上__，为私有属性，类外不能直接更改
        self.__name = name
        self.__age = age
		#公有属性，且设有默认值
        self.school = "茂一" 

    def __str__(self):
        return "Person >> Name: " + self.__name + "\tAge: " + str(self.__age)\
		+ "\tSchool: " + self.school

    def setAge(self, age):
        self.__age = age


class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "People >> Name: " + self.name + "\tAge: " + str(self.age)

lily = Person("lily", 22)
print(lily)
# lily.__age=110 # 错误
lily.setAge(99)
print(lily)

# kitty = People("kitty", 25)
# print(kitty)
