# encoding=UTF-8
import time


class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.school = "茂一"

    def __str__(self):
        return "Person >> Name: " + self.__name + "\tAge: " + str(self.__age)\
            + "\tSchool: " + self.school

    # 程序结束后，自动调用，清理占用的内存空间
    def __del__(self):
        print("--------调用__del__方法--------")

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

lily = Person("lily", 22)
print(lily)
lily.setAge(99)
print(lily)
# del lily
# 延时3s，再销毁对象
time.sleep(3)
