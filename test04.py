# encoding=UTF-8

i = 1
while i <= 5:
    # print("* "*i)
    j = 1
    while j <= i:
        if j == i:
            print("*", end="")  # 不换行
        else:
            print("* ", end="")
        j += 1
    print()
    i += 1
