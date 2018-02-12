# encoding=utf-8
# 求输入N个数的和、平局值


def sumThreeNums(nums):
    # 结果集
    result = []
    # 求和
    sumResult = sum(nums)
    result.append(sumResult)
    # 求平均值
    result.append(sumResult / len(nums))
    # 返回的是列表
    return result


def main():
    # 存放参与运算的数据的列表
    nums = []
    loops = int(input("Please input numbers:"))
    # 输入参与运算的数据
    i = 0
    while i < loops:
        num = int(input())
        nums.append(num)
        i += 1
    # 返回的是列表
    return sumThreeNums(nums)

result = main()
print(result)
print("求和为：%d" % result[0])
print("平均值为：%.2f" % result[1])
