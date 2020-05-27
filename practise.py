"""
写一个函数，输入 lst = [1, 1, 3, 4, 4, 1]，返回值为[1,3,4,1]
"""

# lst = input("Please input a list: ")
lst = [1, 1, 3, 4, 4, 1]
#lst = 3
# print("lst: ",end="")
# print(lst)

def do_list(lst):
    if not isinstance(lst,list):
        exit()
    for item in lst:
        if not isinstance(item,int):
            exit()
    list_len = len(lst)
    i = 0
    lst2 = []
    while i +1  < list_len:
        if lst[i] == lst[i+1]:
            pass
        else:
            lst2.append(lst[i])
        i+=1
    lst2.append(lst[i])
    return lst2

lst2 = do_list(lst)
print("lst2: ",end="")
print(lst2)


