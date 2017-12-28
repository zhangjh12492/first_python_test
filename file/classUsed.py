
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()


class people:
    name =''
    age = 0
    _weight = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('{0} 说：我 {1} 岁。'.format(self.name, self.age))

p = people('runoob', 10, 30)
p.speak()
print(p.name)
print(p._weight)
