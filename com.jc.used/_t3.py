
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和 为：%d" % (counter, sum))

var =1
while var == 1:
    try:
        num = int(input("输入一个数字"))
        print("你输入的数字是", num)
        a = 10
    except ValueError:
        print("输入错误，退出程序")
        break
print("good bye")

for a in (1,3,4,5,6):
    print(a)
else:
    print("dd")

for a in range(1, 30):
    print(a)

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for x in sites:
    if x == "Taobao":
        print("菜鸟")
        break
    print("循环数据：", x)
else:
    print("没有循环数据")
print("循环完成")

for i in range(0,10,3):
    print(i)

a = ["google", 'baidu', 'taobao', 'jingdong']
for i  in range(len(a)):
    print(i, a[i])

print(list(range(6)))


for l in 'runoob':
    if l == 'b':
        break
    print('当前字母为：', l)
var = 10
while var > 0:
    print("当期变量为：", var)
    var -=1
    if var == 5:
        break
print('good bye')

print("------------continue-----------")
for l in 'runoob':
    if l == 'o':
        continue
    print('当前字母:',l)
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print("当前变量值：", var)
print("good bye!")


for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于',x, '*', n//x)
            break
    else:
        print(n, "是质数")

i = 1
while i<=9:
    j =1
    while j <= 9:
        mut = j*i
        print('%d * %d = %d' % (j , i, mut), end='\t')
        j += 1
    print('')
    i += 1

for i in range(1,6):
    for j in range(1, i+1):
        print("* ", end="")
    print()

for i in range(0,5):
    for j in range(1, 5-i):
        print("* ",end="")
    print()

print("---------------===========----------")
# for i in range(0,5):
    # for j in range(1, ):


import sys
def fibonacci(n): #生成器函数- 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f是一个迭代器，由生成器返回生成


while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

print("-----------------------")


def fibonacci(n, w=0): # 生成器函数 - 斐波那契
    a, b, counter= 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1


f = fibonacci(10,0) #f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()