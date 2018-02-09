dictionary = {
    "name": "test",
    "age": 22,
    "gender": "man",
    "email": "abc@qq.com"
}
print(dictionary)
print(dictionary["gender"])  # 不可以取没有的key，会报错
print(dictionary.get("age"))  # 推荐使用，可以取没有的key，不会报错
print(dictionary.get("qq", "12456789"))  # 后面的参数是默认值，若没有此key，则用此默认值；若有，则不用
