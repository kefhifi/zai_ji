
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(''.join(x))
print(x)
print("......")

string = ""
for a in x:
    string += a
print("string: " + string)

print(".........1......")
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[::-2])

print("-------闭包--------")
def outer(a):
    def inner(y):
        nonlocal a
        a += y
        return a
    return inner


fun = outer(0)
print(fun(3))  # 输出：3
print(fun(5))  # 输出：8     # a的取值是上次调用结束的， 闭包具有保留现场的作用
print(fun(6))  # 输出：14



