# isinstance() 函数来判断一个对象是否是一个已知的类型
# lst = [1, 1, 3, 4, 4, 1]
# isinstance(lst,list)
# a=1
# print(isinstance(a,int))

arr = {"int": "整数", "float": "浮点", "str": "字符串", "list": "列表", "tuple": "元组", "dict": "字典", "set": "集合"}
# 判断键是否存在
if "字符串" in arr.keys():
    print("存在")
else:
    print("不存在")
# 判断值是否存在
if "字符串" in arr.values():
    print("存在")
else:
    print("不存在")