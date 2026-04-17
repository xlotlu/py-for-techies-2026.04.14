import math


class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f"Vector({self.length}, {self.angle})"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return str(self.as_tuple())

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        distance = math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )
        angle = 15 # în loc de trigonometrie
        return Vector(distance, angle)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def as_tuple(self):
        return (self.x, self.y)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2
        )

# exemple:
p = Point(5, 7)
p.x
p.y

p.translate(2, 5)
p.x, p.y

f'punctul meu este {p}!!'

Point(5, 7) + Point(5, 8)
Point(5, 8) - Point(3, 2)

Point(5, 7) == Point(5, 7)
Point(5, 7) < Point(5, 8)

if Point(0, 0):
    print("adevărat")
else:
    print("fals")

Point(3, 4).distance_from_origin



# decoratorul este "ceva" ce modifică o funcție in-place
from functools import cache

@cache
def myrand(a, b):
    return random.randint(a, b)
# myrand(1, 100)
# myrand(1, 100)
# myrand(2, 100)
# myrand(2, 100)
# myrand(2, 82)
# myrand(2, 82)
# myrand(2, 100)
# myrand(1, 100)
