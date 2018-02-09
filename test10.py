# encoding=UTF-8
# len()：键值对个数、字符串长度、列表长度...
# keys() : 取出全部的key
# values() : 取出全部的value值
# items() : 返回一个包含所有键值对的元组的列表，一个键值对对应一个tuple，字典对应列表


dictionary = {
    "name": "test",
    "age": 22,
    "gender": "man",
    "email": "abc@qq.com"
}
print(len(dictionary))
print(len(dictionary.get("email")))
print("=" * 50)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print("=" * 50)
# 形如a,b,c = 11,22,33
for key, value in dictionary.items():
    print(key, value)
    # print("key=%s,value=%s" % (key, value))
print("=" * 50)
