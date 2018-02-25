# encoding=UTF-8
# 继承


class Person(object):

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        msg = "Name: %s,  Gender :  %s  Age : %d" % (
            self.name, self.gender, int(self.age))
        return msg

    def __del__(self):
        print("Person destroy...")

# 继承，把父类替换object


class Student(Person):

    def printInfo(self):
        msg = "Inherit Person class: \n"
        msg += "Name: %s,  Gender :  %s  Age : %d" % (
            self.name, self.gender, int(self.age))
        print(msg)

    def __del__(self):
        print("Student destroy...")

kitty = Student('kitty', 'girl', 18)
kitty.printInfo()
