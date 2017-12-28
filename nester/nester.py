import sys


def print_lol(item_list, indent=False, level=0, fn=sys.stdout, ):
    for item in item_list:
        if isinstance(item, list):
            print_lol(item, indent, level + 1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=fn)
            print(item, file=fn)


movies = [
    "新警察故事", [
        "成龙", ["吴彦祖", "谢霆锋", ["178", 75]]
    ], 2003,
    "尖峰时刻", ["成龙", "罗伯特"], 2007
]

# print_lol(movies)
# print("---------------------")
# print_lol(movies, True, 0)
