

print("Hello world!!!")
print(r"\n hello work")

a = """ffffffffffff
ffffffffffff
fffffffffff
ffffff"""
print(a)



import sys; x = 'aaaa'; sys.stdout.write(x+"\n")
print(sys.api_version)
print(sys.hash_info)
for a in sys.hash_info:
    print(a)
print(x , end="")
print("bbb"+x, end="")

print()
print("-----------------")

from sys import hash_info
for a in hash_info:
    print(a)



