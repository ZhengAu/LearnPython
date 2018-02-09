# encoding=UTF-8
# 计算1-100的和，偶数even和，奇数odd和
import time
allResult = 0
evenResult = 0
oddResult = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        evenResult += i
    else:
        oddResult += i
    allResult += i
    i += 1
# time.sleep(0.11)
print("全部和是：%d" % allResult)
print("偶数和是：%d" % evenResult)
print("奇数和是：%d" % oddResult)

# 奇数：2500

# 偶数：2550
# 总和：5050
#


# result = 0
# i = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)
