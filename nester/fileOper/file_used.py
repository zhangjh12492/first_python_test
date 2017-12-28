import os

print(os.getcwd())
# 选择操作的文件夹
os.chdir("../")
print(os.getcwd())

data = open("sketch.txt")
print(data.readline())
print(data.readline())
# 退回到文件起始位置
data.seek(0)
print("------------------------")
for each_line in data:
    print(each_line, end='')
data.close()
print()
print("*********************************")

data = open('sketch.txt')
for each_line in data:
    if each_line.find(":") >-1:
        (role, line_spoken) = each_line.split(":", 1)
        print(role, end="")
        print(' said: ', end='')
        print(line_spoken, end='')



print("*********************************")
print("*********************************")
