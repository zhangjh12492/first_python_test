import sys, os

try:
    path = os.getcwd()
    abspath = path + '/jj.py'
    f = open(abspath, 'r')
    s = f.readline()
    i = print(s)
    f.close()
except OSError as err:
    print("OS Error :{0}".format(err))
except ValueError:
    print("Count not convert data to an integer.")
except:
    print("unexpected error:",sys.exc_info()[0])
else:
    print("no exception")


import os
path = os.getcwd()
abspath = path + '/fileOper1.py'
print(path)
print(abspath)
f = open(abspath, 'r')
print(f.readline())
f.close()

try:
    raise NameError("Hi error")
except:
    print("an exception flew by")
    raise
