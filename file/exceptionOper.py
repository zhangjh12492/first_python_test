class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occurred, value :",e.value)


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# for line in open('fileOper.py'):
#     print(line, end= ' ')

f = open('project_bak.txt')
for line in f:
    print(line, end=' ')

print()
with open('project_bak.txt') as f:
    for line in f:
        print(line, end =' ')