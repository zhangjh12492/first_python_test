
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a +b

a, b, c = 10,356, 200
print(a, b, c, sep='@')


def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)


for i in range(0,20):
    print(fab(5))


age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("你是在逗我吧")
elif age == 1:
    print('相当于14岁的人。')
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age -2) *5
    print("对应人类年龄:", human)

# 退出提示
input("点击enter退出")

print("------------------------------------")
import random
number = random.choice(range(500))
guess = -1
print("数字猜谜游戏")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

num = int(input("请输入一个数字："))
if num % 2 == 0:
    if num %3 == 0:
        print("你输入的数字可以整除2 和 3")
    else:
        print("你输入的数字可医政处2 但不可以整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3但不可以整除2")
    else:
        print("你输入的数字不能整除2和3")