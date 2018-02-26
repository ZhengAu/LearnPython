# encoding=UTF-8
import time

try:
    f = open("../first.py", "r")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line)
except Exception as e:
    print(e)
finally:
    f.close()
    print("文件关闭")
