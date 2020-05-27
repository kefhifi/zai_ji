"""
现在要写一个函数search，当给search函数传入‘金字塔’的 时候，函数打印出奴隶社会.非洲.古埃及文明.金字塔，
当给search函数传入美洲的时候，打印出“不存在的关键字：美洲“
"""
import json
file_name="json.txt"
with open(file_name,encoding="utf-8") as file_obj:
    content=file_obj.read()

content = json.loads(content.encode('utf8')[3:].decode('utf8'))

def search(string, content):
    for key1,value1 in content.items():
        if "洲" in string:
            if string not in value1.keys():
                print("不存在的关键字：" + string)
        for key2,value2 in value1.items():
            for key3,value3 in value2.items():
                if string in value3:
                    print(key1 + "." + key2 + "." + key3 + "." + string)

string="金字塔"
# string="美洲"
search(string, content)

