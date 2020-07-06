
a = [1, 2, 3, 4, 5,6]
b = [i*i for i in a]
print(b)

 c = lambda x, y: x*y

print(list(map(c, a, b)))

