
filepath = '/Users/alex/romance_pro/myPython\
/first_python_test\
/com.jc.used/suc.py'


'''
f = open('/Users/alex/romance_pro/myPython\
/first_python_test\
/com.jc.used/suc.py',
         'r+')
f.write("你好啊\n")
f.write("nihao1\n")
f.write("nihao2\n")
f.write("fsdfsafsd\n")
f.close()

f = open('/Users/alex/romance_pro/myPython\
/first_python_test\
/com.jc.used/suc.py',
         'r+')
print(f.read())
f.close()


f = open(filepath, 'r+')
str = f.readline()
print(str)

f.close()

f = open(filepath, 'r')
str = f.readlines(10)
print(str)
f.close()
print("----------------------")
'''

f = open(filepath, 'r')

for line in f:
    print(line , end='')
f.close()

f = open(filepath, 'w')
value = ('www,cc,eee.r', 344)
s = str(value)
f.write(s)
print(f.tell())
f.close()

from urllib import  request
response = request.urlopen("http://www.baidu.com")
fi = open('project.txt', 'w')
page = fi.write(str(response.read()))
fi.close()





import os
print("当前目录为:",os.getcwd())
print("当前目录所有文件：", os.listdir(os.getcwd()))

os.rename("project.txt","project_bak.txt")
print("当前目录所有文件：", os.listdir(os.getcwd()))