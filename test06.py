# encoding=UTF-8
# 把list列表中文件名称的后缀名提取出来
fileNames = ['01.py', '02.py', '03.txt', '04.rar', '05.zip']
suffixName = []
for temp in fileNames:
    suffixName.append(temp[temp.rfind('.') + 1:])

print("源文件名称：", fileNames)
print()
print("文件后缀名：", suffixName)
print()
print(len(suffixName))
fileNames.reverse()
print(fileNames)
fileNames.sort()
print(fileNames)
