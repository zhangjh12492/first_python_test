def hello():
    print("hello world")


hello()


def area(width, height):
    return width * height


def print_welcome(name):
    print("welcome", name)


print(print_welcome("xiaoming"))

w =4
h = 5
print("width=",w, ",height = ",h, ",area = ", area(w, h))


a = 10
def test():
    global a
    a = a+ 1
    print(a)



def dec(name, *args):
    print("name : ",name)
    for i in args:
        print(i, end=' ')


dec("ccc",1334,"jie",333,"fff")

print("------------------")
vec = [2, 4, 6]
_list = [3*x for x in vec]
print(_list)


print("=================")
_list1= [[x, x**2] for x in vec]
print(_list1)
print("-==--------")
freshfruit = ['banana    ', '   loganberry  ', '   passion fruit  ']
_fruit_list = [weapon.strip() for weapon in freshfruit]
print(_fruit_list)
print("****************************************")
_list2 = [3*x for x in vec if x > 3]
print(_list2)
print("****************************************")
_list3 = [3*x for x in vec if x < 2]
print(_list3)
print("****************************************")

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
_list4 = [x*y for x in vec1 for y in vec2]
print(_list4)
print("****************************************")
_list5 = [x+y for x in vec1 for y in vec2]
print(_list5)
print("****************************************")
_list6 = [vec1[i] * vec2[i] for i in range(len(vec1))]
print(_list6)
print("****************************************")

_list7 = [str(round(355/113, i)) for i in range(1, 6)]
print(_list7)
print("****************************************")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix_exchange = [[row[i] for row in matrix] for i in range(4)]
print(matrix_exchange)
print("****************************************")
for row in matrix:
    print(row)
print("****************************************")

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print("****************************************")

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
print("****************************************")

basket = {'apple', 'pear', 'apple', 'pear', 'orange', 'orange'}
print(basket)
print('orange' in basket)
print('ddd' in basket)
print("****************************************")

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)   # 在 a 中的字母，但不在 b 中
print(a | b)     # 在 a 或 b 中的字母
print(a & b)    # 在 a 和 b 中都有的字母
print(a ^ b)     # 在 a 或 b 中的字母，但不同时在 a 和 b 中
print("**********************************")
a = {x for x in 'abracadabra' if x not in 'alacazam'}
print(a)
print("************************************")
tel = {'jack':5555, 'soc':6324}
tel['mecc'] = 9999
print(tel)
print(tel['jack'], tel['mecc'])
tel['ivr'] = 8779
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('ivr' in tel)
print('mecc' not in tel)
print("*************************************")
print(dict([('saaa',333),('mmmm',344),('eeee',6334)]))

_dict = {x: x**2 for x in (2, 4, 6)}
print(_dict)
print(dict(sape =3443, guide=344))

knights = {'gallfds':'tree', 'robin':'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'jue']):
    print(i, v)

print("******************************")
questions = ['name', 'age', 'weight', 'height']
answers = ['jcc', 43, 65, 166]
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))
print("*******************************")
for i in reversed(range(1,10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'banana', 'orange']
for f in sorted(set(basket)):
    print(f)
print("******************")
# 元组不可变，若元组成员可变，则成员可编辑
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10, 11, 12]
t = a, b, c
print(t)
del b[1:4]
print(t)

print("********************")
_c = [x*y for x in range(1,5) if x > 2 for y in range(1,4) if x <4]
print(_c)
for x in range(1,5):
    if x > 2:
        for y in range(1,4):
            if x < 4:
                print(x*y)