# encoding=UTF-8


f = open('abc.py', 'r')

for line in f.read():
    print(line, end='')

# print()

fp = f.read()
print(fp)

f.close()
