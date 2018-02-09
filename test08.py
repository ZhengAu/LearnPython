# encoding=UTF-8
# 把8个老师随机安排到3个办公室内
# 应该每个办公室至少有2个老师，最多3个
# 缺点：当添加办公室或老师人数时，程序缺乏灵活性

import random
offices = [[], [], []]
teachers = ["A老师", "B老师", "C老师", "D老师", "E老师", "F老师", "G老师", "H老师"]

for teacher in teachers:
    index = random.randint(0, 2)
    if len(offices[index]) < 3:  # 当前index办公室的老师人数<3，则添加
        offices[index].append(teacher)
    # index为2，且index办公室的人数>=3，则放到其他办公室
    elif len(offices[index]) >= 3 and index == 2:
        if len(offices[index - 1]) >= 3:  # index为1>=3，则放到0
            offices[index - 2].append(teacher)
        else:
            offices[index - 1].append(teacher)
    elif len(offices[index]) >= 3 and index == 1:
        if len(offices[index - 1]) >= 3:
            offices[index + 1].append(teacher)
        else:
            offices[index - 1].append(teacher)
    elif len(offices[index]) >= 3 and index == 0:
        if len(offices[index + 1]) >= 3:
            offices[index + 2].append(teacher)
        else:
            offices[index + 1].append(teacher)

for office in offices:
    print(office)
