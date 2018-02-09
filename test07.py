# encoding=UTF-8
# 把8个老师随机安排到3个办公室内
# 应该每个办公室至少有2个老师，最多3个
import random
offices = [[], [], []]
teachers = ["A老师", "B老师", "C老师", "D老师", "E老师", "F老师", "G老师", "H老师"]

for teacher in teachers:
    index = random.randint(0, 2)
    print(index, end=" ")
    offices[index].append(teacher)

print()
for office in offices:
    print(office)
    print("长度：", len(office))
