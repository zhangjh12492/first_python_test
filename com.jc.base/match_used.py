# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

print("------------------re.search, re.match-------------------")
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r"dogs", line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group()", matchObj.group())
else:
    print("No match!")

matchObj = re.search(r"dogs", line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group()", matchObj.group())
else:
    print("No match!")

print("------------- re.sub ----------------")

phone = "2004-959-959 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$',"", phone)
print("电话号码：",num)

# 移出非数字内容
num = re.sub(r'\D', "", phone)
print("电话号码：",num)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    print(value)
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

print("---------------")