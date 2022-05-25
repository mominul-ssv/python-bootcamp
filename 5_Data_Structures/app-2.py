from collections import deque
from array import array
from sys import getsizeof

from numpy import number

print("# ================================== Zip Function ================================== #")
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# [(1, 10), (2, 10), (3, 30)]
zipped = list((zip(list1, list2)))
print(zipped)

zipped = list((zip("abc", list1, list2)))
print(zipped)

print("# ================================== Stacks ================================== #")
# LIFO (Last In - First Out)

# push
browing_session = []
browing_session.append(1)
browing_session.append(2)
browing_session.append(3)
print(browing_session)

# pop
last = browing_session.pop()
print(last)
print(browing_session)
print("redirect", browing_session[-1])

# check if the stack is empty
# 0, "", [] all of these defines something empty
# not browsing_session = not empty = False
if not browing_session:
    print("disable")
else:
    print("keep back-button enabled")

print("# ================================== Queues ================================== #")
# FIFO (First In - First Out)

# import deque from the collection module
queue = deque([])

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

# deque
queue.popleft()
print(queue)

# check if the queue is empty
if not queue:
    print("empty")
else:
    print("list is not empty")


print("# ================================== Tuples ================================== #")
point = 1, 2
print(type(point))

# python will treat this as an integer
point = 1
print(type(point))

# python will treat this as a tuple
point = 1,
print(type(point))

# empty tuple
point = ()
print(type(point))

# tuple concatenation
point = (1, 2) + (3, 4)
print(point)

# multiple a tuple
point = (1, 2) * 3
print(point)

# convert a list of numbers into a tuple
point = tuple([1, 2])
print(point)

# convert a list of string into a tuple
point = tuple("Hello World")
print(point)

# get item(s) from a tuple
point = (1, 2, 3)
print(point[0:2])

x, y, z = point
if 3 in point:
    print("exists")

# note: tuples cannot be overridden

print("# ================================== Swapping Variables ================================== #")
x = 10
y = 11
print("x:", x, "y:", y)

z = x
x = y
y = z
print("x:", x, "y:", y)

# simplified version
# here, we are defining a tuple
# x, y = (y, x)
# left side of the code is unpacking the tuple
x, y = y, x
print("x:", x, "y:", y)

# the code above explains why we can define multiply variables at the same line
a, b = 1, 2
print("a:", a, "b:", b)

print("# ================================== Arrays ================================== #")
# import array from the array module

# Google python 3 typecode

# Type code     C Type                   Python Type           Minimum size in bytes
# ============================================================================
# 'b'           signed char              int                   1
# 'B'           unsigned char            int                   1
# 'u'           wchar_t                  Unicode character     2
# 'h'           signed short             int                   2
# 'H'           unsigned short           int                   2
# 'i'           signed int               int                   2
# 'I'           unsigned int             int                   2
# 'l'           signed long              int                   4
# 'L'           unsigned long            int                   4
# 'q'           signed long long         int                   8
# 'Q'           unsigned long long       int                   8
# 'f'           float                    float                 4
# 'd'           double                   float                 8

numbers = array('i', [0, 2, 3])

# change items by index
numbers[0] = 1

# add at the end of the array
numbers.append(4)
print(numbers)

# add at a specific index
numbers.insert(0, 45)
print(numbers)

# remove the last index item from the array
numbers.pop()
print(numbers)

# remove a specific item fro the array
# make sure to put it insidea an if-else block
numbers.remove(45)
print(numbers)

print("# ================================== Sets ================================== #")
numbers = [1, 1, 2, 3, 4]

# we use set to remove duplicates
# convert the array to a set
unique = set(numbers)
print(unique)

# defining a set
second = {1, 7}
print(second)

# add
second.add(5)
print(second)

# remove
second.remove(5)
print(second)

# length of a set
print(len(second))

print("=============================================")
first = {1, 3, 5, 7}
second = {1, 2, 4, 6, 8}

# union of two sets
print(first | second)

# intersection of two sets
print(first & second)

# difference between two sets
# this will return {3, 5, 7} which means the first set has some additional numbers that we don't have in the second set
print(first - second)

# symmetric difference
# this will return return it numbers which are not in both of the sets
print(first ^ second)

# note: we cannot access the elements of set using index
# we can use if-else to check an items existence in a set
if 1 in first:
    print("yes")

print("# ================================== Dictionaries ================================== #")
# dictionaries work as key-value pairs
point = {"x": 1, "y": 2}
print(point)

# using dictionary built-in function
point = dict(x=3, y=4)
print(point)

# printing an element
print(point["x"])

# chaning the value of a key
point["x"] = 10
print(point)

# add a new key-value pair
point["z"] = 20
print(point)

print("=============================================")
# if the key is not matched then it will return an error; thus, we have to use if-else condition
if "a" in point:
    print(point["a"])
else:
    print("Item doesn't exit")

# simplified
print(point.get("a"))

# return 0 if no item is found
print(point.get("a", 0))

# delete an item
del point["z"]
print(point)

print("=============================================")
# looping over items in dictionary
# method-1
for key in point:
    print(key, point[key])

# method-2
# in each iteration we will get tuple
for x in point.items():
    print(x)

# unpack the tuple
for key, value in point.items():
    print(key, value)

print("# ================================== Dictionary Comprehensions ================================== #")
values = []
for x in range(5):
    values.append(x * 2)
print(values)

values = []
values = {x * 2 for x in range(5)}
print(values)

print("=============================================")
values = []
values = {x: x * 2 for x in range(5)}
print(values)

values = {}
for x in range(5):
    values[x] = x * 2
print(values)

print("# ================================== Generator Expressions ================================== #")
# we use this generator object when we have a large dataset
values = []

values = (x * 2 for x in range(5))
print(values)

for x in values:
    print(x)

print("=============================================")
values = []

# the size is 112 and it is fixed.
# note: we cannot use len() function for generator object
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

print("# ================================== Unpacking Operator ================================== #")
# unpacking list
numbers = [1, 2, 3]

print(numbers)
print(*numbers)

print("=============================================")
values = list(range(3))
print(values)

values = [*range(4), *"Hello"]
print(values)

print("=============================================")
first = [1, 2]
second = [3]

values = [*first, "a", *second, *"Hello"]
print(values)

print("=============================================")
# unpacking dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}

# if we have multiple values with the same key then the last value will be used
combined = {**first, **second, "z": 1}
print(combined)
