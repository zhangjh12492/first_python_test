print(5 + 4)

print(4.3 - 2)

print(3 * 7)
print(2 / 4)
print(2 // 4)

print(17 % 3)
print(2 ** 5)

list = ['abcd', 1234, 1234.33, True]
tinylist = [123, 'bbccc']
print(list)
print(list[0])
print(list[0:])
print(list[0:-1])
list[0] = 13344
print(list[-1])
print(list[0:3])
print(list * 2)
print(list + tinylist)
list[0:3] = []
print(list)

tuple = ('abcd', 343, 55.44, True, 'eeee')
tinytuple = ('mmmmm', 'dddd')
print(tuple)
print(tuple[0])
print(tuple[0:3])
print(tuple[0:19])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

student = {"tom", "jack", "mary", 'dikar', 'lanna'}
print(student)
if('tom' in student):
    print('tom in student')
else:
    print("tom isn't in student")

print()
a = set('abcdefg')
b = set('efghij')
print(a)
print(a - b)    #a和b的差集
print(a | b)    # a和b的并集
print(a & b )   # a和b的交集
print(a ^ b)    # a和b不同时存在的元素


dict = {}
dict['one'] = '1 - '
dict[2] = '2 -'
tinydict = {'name':'jcc', 'code':1 }
print(dict)
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

