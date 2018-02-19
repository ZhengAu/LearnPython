# encoding=UTF-8
# class的定义
# Noted: 方法中的self不能省略

class Student:
	
	# 定义属性
	# 如同C++中的构造函数
	def __init__(self):
		self.weight=100
		self.high=178
	def __init__(self,weight,high):
		self.weight=weight
		self.high=high

	# 定义方法	
	def running(self):
		print("I'm running...")
	
	def eating(self):
		print("I'm eating...")

stu1=Student(120,180)
print("------stu1------")
stu1.running()
stu1.eating()

print(stu1.weight)
print(stu1.high)

print("------stu2------")
stu2=Student(110,178)

print(stu2.weight)
print(stu2.high)
