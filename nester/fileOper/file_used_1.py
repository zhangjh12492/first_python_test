import os

# print(os.getcwd())
# 选择操作的文件夹
# os.chdir("../")
# print(os.getcwd())

if os.path.exists('sketch.txt'):
    data = open("sketch.txt")
    for each_line in data:
        (role, line_spoken) = each_line.split(":", 1)
        print(role, end='')
        print(" said :", end='')
        print(line_spoken, end='')
    data.close()
else:
    print('the data file is missing!')


os.chdir("../")
try:
    data = open("sketch.txt")
    for each_line in data:
        if not each_line.find(':')==-1:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(" said :", end='')
            print(line_spoken, end='')
    data.close()
except:
    print('The data file is missing!')

print()
print("---------------------------")

try:
    data = open("sketch.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(" said :", end='')
            print(line_spoken, end='')
        except:
            pass
    data.close()
except:
    print('The data file is missing!')


print('\n\n\n---------------------------\n\n')

try:
    data =open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoker) = each_line.split(':')
            print(role, end='')
            print(' said :', end='')
            print(line_spoker, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')