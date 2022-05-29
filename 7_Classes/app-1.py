# Class: blueprint for creating new objects
# Object: instance of a class

class Point:
    def draw(self):
        print("Drawing a circle.")


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
