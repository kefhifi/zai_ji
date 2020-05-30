
import re

file_name = "report.txt"
pattern = "^[\d\D]+ +[\d]{3,}$"      # 贪婪模式
with open(file_name) as file_obj:
    for line in file_obj:
        result = re.findall(pattern, line)
        if result:
            print(result)



import re

file_name = "report.txt"
pattern = "^[\d\D]+ +[\d]+$"      # 贪婪模式
list_all_data = []
data_dict = {}
with open(file_name) as file_obj:
    for line in file_obj:
        result = re.findall(pattern, line)
        if result:
            list_item = []
            saas=re.findall("^([\w]+) +",result[0])  # 取圆括号里面的字符(saas名称)
            list_item.append(saas[0])
            web = re.findall("^[\w]+ +([\d]+) +",result[0]) # 获取web登录的次数，即数字
            list_item.append(int(web[0]))
            client = re.findall(" +([\d]+)$",result[0])  # 获取客户端登录次数 ，即数字
            list_item.append(int(client[0]))
            print(list_item)
            list_all_data.append(list_item)
print(list_all_data)
# 下面这个lambda 表达式不行，因为返回的只是列表中的最后一个元素为0，要返回这列表为空 应该才可以达到要求（剔除小于100的列表元素）
lam = lambda list_item : [list_item[0],list_item[1],list_item[2] if list_item[2] >= 100 else 0]
def bigger_litter(list_item):
    if list_item[2] >= 100:
        return list_item
    else:
        return 0
"""
filter(function, iterable)
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
result_done = filter(bigger_litter, list_all_data)
list_done = list(result_done)
print(list_done)
for item in list_done:
#   print(item[0] + " " + str(item[1]) + " " + str(item[2]))
    print(f'{item[0]}  {item[1]}  {item[2]}')


"""
map(function, iterable, ...)
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""

la = lambda x : x*x
a = [2,3,4,5]
b = map(la, a)
print(list(b))

