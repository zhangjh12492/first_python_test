class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('{0} 说：我 {1} 岁，{2}cm 高'.format(self.name, self.age, self.__weight))


# 单继承实例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print('{0} 说：我 {1} 岁，{2}cm 高, 我在读 {3} 年级'.format(self.name, self.age, self.__weight, self.grade))


class Speaker():
    topic = ''
    name = ''

    def __init__(self, n ,t):
        self.name =n
        self.topic = t

    def speak(self):
        print("我叫{0}， 我是一个演说家，我演讲的主题是{1}".format(self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample('Tim', 15, 153, 7, 'python')
test.speak()