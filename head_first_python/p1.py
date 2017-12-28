

def print_lol(item_list):
    for item in item_list:
        if isinstance(item, list):
            print("--> this is a list, continue")
            print_lol(item)
        else:
            print("-->",item)


movies = [
    "新警察故事",[
        "成龙",["吴彦祖","谢霆锋",["178",75]]
    ],2003,
    "尖峰时刻",["成龙","罗伯特"],2007
]
print_lol(movies)