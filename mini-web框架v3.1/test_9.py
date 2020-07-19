
a = [1, 2, 3, 4, 5,6]
b = [i*i for i in a]
print(b)

c = lambda x, y: x*y

print(list(map(c, a, b)))
# 匿名函数可以这样传递参数求值
print(c(2,3))

