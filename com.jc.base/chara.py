
a = 'a' \
    'aaa'
print(a)

b = 'b\\bbb'
print(b)

c = 'c\'cc'
print(c)

d = 'd"dd'
e = "e\"eee"

f = 'fff\afff'
print(f)

g = 'gg\bggg'
print(g)

h = 'hh\fhhh'
print(h)


print(h.capitalize())

print(h.center(20,'a'))
print(h.__len__())
print(h.count('h',0, 10))


print(h.encode('utf-8' ))
print(h.encode().decode())

i = 'iiii\tiiii'
print(i)
print(i.expandtabs(20))
print(i.expandtabs())


print(i.find('\t'))

# print(i.index('f'))

print('------- jj ----------')
j = 'jjj'
print(j.isalnum())
print(''.isalnum())
print('ff33'.isalnum())
print('333'.isalnum())

print('========================================================================')

print('3333'.isnumeric())
print('333333dd'.isnumeric())
print('333333-+-'.isnumeric())

print(len(j))


print('bbb'.ljust(4)+'j')
print('ccc'.rjust(5))

print('b   ccc'.lstrip('b'))


print('bb,cc,eed,ff'.split(',', 1))

print('-----------------')
intab = 'is'
outtab = '34'
trantab = str.maketrans(intab, outtab)
print(trantab)
print('this is a example '.translate(trantab))
