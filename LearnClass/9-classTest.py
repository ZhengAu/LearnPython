# encoding=UTF-8
# 定义为公有属性


class Animal(object):  # 基类

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        msg = "Name:%s, Color:%s" % (self.name, self.color)
        return msg

    def eat(self):
        print("---" + self.name + " 在eat...---")

    def bark(self):
        print("---" + self.name + " 在bark...---")

    def run(self):
        print("---" + self.name + " 在run...---")


class Horse(Animal):  # 马类

    def bark(self):
        print("---啊啊啊啊啊啊...---")

    def run(self):
        print("---" + self.name + "跑的很快...---")


class Donkey(Animal):  # 驴类

    def bark(self):
        print("---咩咩咩咩咩咩...---")

    def run(self):
        print("---" + self.name + "跑的慢...---")


class HanxueBaoma(Horse):  # 汗血宝马类

    # 重新定义
    # 可在基类中默认颜色为血红色，或者不需要此方法在创建对象时传参给color
    def __init__(self, name, color="血红色"):
        self.name = name
        self.color = color

    def bark(self):
        print("---哈哈哈哈哈哈...---")

    def run(self):
        print("---" + self.name + "跑的超快...---")


class Mule(Horse, Donkey):  # 骡子类

    def bark(self):
        print("---嘘嘘嘘嘘嘘嘘...---")

    def run(self):
        print("---" + self.name + "跑的超慢...---")


# ==============================================
print("===============Horse===============")
horse = Horse('中华汉马', '百色')
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
