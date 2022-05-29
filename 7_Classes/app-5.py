from abc import ABC, abstractclassmethod, abstractmethod
from collections import namedtuple

print("# ================= abstract base classes ================= #")


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened!")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")

# the read method is not instantiated, thus following code will give us an error
# stream = Stream()


# this read method has been instantiated in the following classes, thus they will not give any errors
stream = FileStream()
stream.read()
stream = NetworkStream()
stream.read()
stream = MemoryStream()
stream.read()

print("# ================= polymorphism ================= #")


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])

print("# ================= duck typing ================= #")


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])

print("# ================= extending built-in types ================= #")


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
list.append("2")

print("# ================= data classes ================= #")

# method-1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

# magic methods must be implemented to accurately compare these two methods
print(p1 == p2)

# printing memory location
print(f"p1: {p1} \np2:{p2}")

print("# ================================== #")

# method-2 (better approach)
# must import the 'collection' module
# must import 'namedtuple'
# benefit: we don't need to explicitly define magic methods
# constraints: once we assign a value, we can't override it, thus a 'namedtuple' immutable

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
