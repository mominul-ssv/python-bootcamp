print("# ================= inheritance & the object class ================= #")


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, Mammal))

# Animal: Parent/Base class
# Mammal: Child/Sub class
# Fish: Child/Sub class
# all classes in python inherits from the 'object' class

print("# ================= method overriding ================= #")


class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

print("# ================= multiple inheritance ================= #")


class Flayer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlayingFish(Flayer, Swimmer):
    pass


print("# ================= good inheritance example ================= #")


class InvalidOperationError(Exception):
    pass


class Stream:
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


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
