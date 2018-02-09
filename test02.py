# encoding=utf-8

import time
print("Please input your number: ")
inputNum = int(input())
row = inputNum//3
column = inputNum % 3

time.sleep(1)
print("%s is in %d row %d column." % (inputNum, row, column))
print(inputNum, "在", row, "行", column, "列")
comp = complex(row, column)
print(comp)
