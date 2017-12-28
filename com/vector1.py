

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b)

    def __divmod__(self, other):
        return Vector(self.a / other.a, self.b / other.b)

    def __mod__(self, other):
        return Vector(self.a % other.a, self.b % other.b)

    def __ipow__(self, other):
        return Vector(self.a )


v1 = Vector(2, 10)
v2 = Vector(4, -5)

print(v1 + v2)