# encoding=UTF-8
# 定义私有属性
# 用方法来获取私有属性


class Animal(object):  # 基类

    def __init__(self, name, color="血红色"):
        self.__name = name
        self.__color = color

    def __str__(self):
        msg = "Name:%s, Color:%s" % (self.getName(), self.getColor())
        return msg

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def eat(self):
        print("---" + self.getName() + " 在eat...---")

    def bark(self):
        print("---" + self.getName() + " 在bark...---")

    def run(self):
        print("---" + self.getName() + " 在run...---")


class Horse(Animal):  # 马类

    def bark(self):
        print("---啊啊啊啊啊啊...---")

    def run(self):
        print("---" + self.getName() + "跑的很快...---")


class Donkey(Animal):  # 驴类

    def bark(self):
        print("---咩咩咩咩咩咩...---")

    def run(self):
        print("---" + self.getName() + "跑的慢...---")


class HanxueBaoma(Horse):  # 汗血宝马类

    # def __init__(self, name, color="血红色"):
    #     Animal.__init__(self, name, color)
    #     # super().__init__(name, color)
    #     # super().__init__(name)  # 仅仅设置name,color使用父类默认的

    def bark(self):
        print("---哈哈哈哈哈哈...---")

    def run(self):
        print("---" + self.getName() + "跑的超快...---")


class Mule(Horse, Donkey):  # 骡子类

    def bark(self):
        print("---嘘嘘嘘嘘嘘嘘...---")

    def run(self):
        print("---" + self.getName() + "跑的超慢...---")


# ==============================================
print("===============Horse===============")
horse = Horse('中华汉马', '白色')
horse.eat()
horse.bark()
horse.run()
print(horse)

print("\n===============Donkey===============")
donkey = Donkey("驴子星", "黝黑色")
donkey.eat()
donkey.bark()
donkey.run()
print(donkey)

print("\n===============HanxueBaoma===============")
hanxuebaoma = HanxueBaoma("汗血宝马")
hanxuebaoma.eat()
hanxuebaoma.bark()
hanxuebaoma.run()
print(hanxuebaoma)

print("\n===============Mule===============")
mule = Mule("骡子拐", "黑色")
mule.eat()
mule.bark()
mule.run()
print(mule)
print("==============================")
# ==============================================
