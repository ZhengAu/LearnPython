# encoding=UTF-8


try:
    print("---- test 1 ----")
    f = open("../first.py", "r")
    print("---- test 2 ----")
    print(num)
except Exception as e:
    print(e)
finally:
    f.close()
