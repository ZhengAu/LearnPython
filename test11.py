# encoding=utf-8
# 打印横线


def printLine():
    print("-" * 30)


def printLinesByNums(num):
    i = 0
    while i < num:
        printLine()
        i += 1

lines = int(input("Please input line numbers:"))

printLinesByNums(lines)
