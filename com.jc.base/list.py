

print("====================")
list_2d = [[0 for col in range(4)] for row in range(4)]
print(list_2d)
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(6)
list_2d[3].append(4)
print(list_2d)


l = [i for i in range(0,15)]
print(l[::2])

print("---------------------------------------")
a = [1, 2, 3]
b = a
c = []
c = a
d = a[:]

print(a, b, c, d)

b[0] = 'b'
print(a, b, c, d)

print(id(a), id(b), id(c), id(d))

c[0] = 'c'
print(a, b, c, d)

import copy
a = [1, 2, 3, 4]
b = a
d = copy.copy(a)
b[0] = 'b'
print(a, b, d)
print(id(a), id(b), id(d))





print()
print("-----------------dictionary--------")
dict_1 = {'name':'jcc', 'age':13}
print(dict_1)
dict_2 = dict_1.copy()
print(dict_1, dict_2)
print(id(dict_1), id(dict_2))

seq_1 = ['name', 'age', 'address']
dict_3 = dict_1.fromkeys(seq_1)
print(dict_3)
dict_3 = dict_1.fromkeys(seq_1, 1)
print('dict_3 : %s' %(str(dict_3)))
print('dict_1 : %s, dict_3: %s' % (dict_1, dict_3))

print(dict_3.items())

print('dict_3.name : %s' % dict_3.get('name'))
print('key name in dict_3 : %s' % ('name' in dict_3))

print("ergodic dict_3 : ", end='')
for i in dict_3:
    print(str(i)+',', end='')
print()
print('ergodic dict_3.keys : ', end='')
for i in dict_3.keys():
    print(str(i)+',', end='')
print()
print('ergodic dict_3.values : ', end='')
for i in dict_3.values():
    print(str(i)+',', end='')

print('ergodic dict_3.values : ', end='')
for i in dict_3.items():
    print(i[0]+":" + str(i[1]))


dict_3.update({'name' : 'xiaoxiao'})
print(dict_3)

dict_3.pop('name')
print(dict_3)

c = dict_3.popitem()
print('c, key: %s, value: %d' % (c[0],  c[1]))
print(dict_3)

print("--------------多级map----------------")

cities = {
    '北京': {
        '海淀':['圆明园', '清河', '小营桥', '中关村', '北京大学'],
        '朝阳': ['国贸', 'CBD', '世贸天阶'],
        '昌平': ['沙河', '高教园']
    },
    '河北': {
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for i in cities['北京']:
    print(i)
print('---------')
for i in cities['北京']['海淀']:
    print(i)
print('----------')

