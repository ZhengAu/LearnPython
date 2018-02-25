# encoding=UTF-8
# 继承
# 私有属性、方法，不能被继承
# 前面加 __ 则表示私有方法、私有属性

# 继承object


class Person(object):

    def __init__(self, name, gender, age):
        self.__name = name  # 私有方法不能被继承，只能在本类中使用
        self.__gender = gender
        self.__age = age

    # 私有方法，不能被继承或者在外界调用
    def __printInfo(self):
        msg = "------Person's printInfo()------\n"
        msg += "Name:%s,  Gender:%s,  Age:%d  " % (
            self.__name, self.__gender, self.__age)
        print(msg)

    def printInfo2(self):  # 哪个对象不再被调用，则会被删除
        self.__printInfo()  # 调用私有方法

    def __del__(self):
        print("Person destroy...")

# 继承，把父类替换object
# 只能调用公有方法printInfo2(),不能调用私有方法__printInfo()


class Student(Person):

    def __del__(self):
        print("Student destroy...")

    # 重写父类的方法
    def printInfo2(self):
        msg = "------Student's printInfo()------\n"
        msg += "\t\t--重写父类的方法--"
        print(msg)
        # 调用父类的方法，还需父类的一部分功能
        # 注意区别，一个要self，一个不要
        Person.printInfo2(self)
        super().printInfo2()

kitty = Person('kitty', 'girl', 18)
# kitty.__printInfo() # 错误，不能在类外调用私有方法
kitty.printInfo2()

marry = Student("Marry", 'girl', 20)
marry.printInfo2()

# 先Person destroy...
# 后Student destroy...
