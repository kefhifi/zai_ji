
# 测试输入空字符串的情况，int 时会报错
port = input("input name :")
print("1:")
print(port)
if port:
    print("非空字符串")
else:
    print("空字符串")
port = int(port)
print("2:")
print((port))
if port:
    print("非零")
else:
    print("零")


