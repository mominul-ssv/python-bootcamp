print("# ================= defining a constructor ================= #")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

print("# ================= class vs instance attributes ================= #")


class Point:
    # class attributes
    # class attributes are shared across all instances of a class
    default_color = "blue"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# instance attributes
point = Point(1, 2)
print(point.default_color)  # using reference
point.draw()

Point.default_color = "green"

point = Point(3, 4)
print(Point.default_color)  # using Point class
point.draw()

print("# ================= class vs instance methods ================= #")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()

print("# ================= magic methods ================= #")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(5, 6)
print(point)

print("# ================= comparing objects ================= #")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


pointOne = Point(6, 7)
pointTwo = Point(6, 7)
pointThree = Point(5, 6)
print(pointOne == pointTwo)
print(pointOne > pointThree)
print(pointOne < pointThree)

print("# ================= performing arithmetic operations ================= #")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)

# this will print a new combined point object
# to view the values of that object, we can use the __str__ magic method
print(point + other)

# this will print the value of the point object
combined = point + other
print(f"x: {combined.x}, y: {combined.y}")
