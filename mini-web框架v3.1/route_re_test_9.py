import re

a = [1, 2, 3, 4, 5,6]
b = [i*i for i in a]
print(b)

c = lambda x, y: x*y

print(list(map(c, a, b)))
# 匿名函数可以这样传递参数求值
print(c(2,3))
print("-----------分割线-3------")

dic_test = {
    r"/index.html": 1,
    r"/add/\d+\.html": 2
}

# file_name = "/index.html"
file_name = "/add/322323.html"
for url, fun in dic_test.items():
    print(re.match(url, file_name), end="")
    print("---", url, end="")
    print("---", fun)




