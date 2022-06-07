print("# ================================== Lists ================================== #")

# 1D array
letters = ["a", "b", "c"]

# 2D arrays
matrix = [[0, 1], [2, 3]]

# write 0 five times in an array
zeros = [0] * 5

# combine the previous zeros and letters
combined = zeros + letters
print(combined)

# list range (0 to 19 will be printed)
# list function takes any iterable
numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))

print("# ================================== Accessing Items ================================== #")

letters = ["a", "b", "c", "d"]

print(letters[0])

print(letters[-1])

print(letters[0:3])

print(letters[:3])

print(letters[0:])

print(letters[:])

numbers = list(range(20))
print(numbers)

# 0 -> 3 -> 6
print(numbers[::3])

# 0 -> 4 -> 8
print(numbers[::4])

# reverse order
print(numbers[::-1])

print("# ================================== Unpacking List ================================== #")
# =================================================================================== #
numbers = [1, 2, 3]

# method-1
first = numbers[0]
second = numbers[2]
third = numbers[1]

# method-2 (the number of variables must be equal to the total items in the array)
first, second, third = numbers

# =================================================================================== #
numbers = [1, 2, 3, 4, 4, 4, 5, 6]

# [unpack] the first and second element. [pack] the rest of the elements.
first, second, *other = numbers

print(f"first: {first}, second: {second}")
print(f"other: {other}")

# =================================================================================== #
numbers = [1, 2, 3, 3, 3, 4, 5, 6]

# [unpack] the first and last element. [pack] the rest of the elements.
first, *other, last = numbers

print(f"first: {first}, last: {last}")
print(f"other: {other}")

print("# ================================== Looping Over List ================================== #")

letters = ["a", "b", "c"]

# loop over each element
for letter in letters:
    print(letter)

print("=================")
# to get the index of each item use 'enumerate' built-in function
# 'enumerate' keyword returns an 'enumerate' object which is iterable
# in each iteration, the 'enumerate' object will give us a 'tuple'
# a tuple is like a list but read-only
for letter in enumerate(letters):
    print(letter)

print("=================")
for letter in enumerate(letters):
    print(letter[0])

print("=================")
for letter in enumerate(letters):
    print(letter[1])

print("=================")
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("=================")
# if we have a list of 'items', we can unpack it and assigned each items to a variable

# unpacking a list
# items = [0, "a"]
# index, letter = items

# unpacking a tuple
# items = (0, "a")
# index, letter = items

for index, letter in enumerate(letters):
    print(index, letter)

print("# ================================== Adding or Removing Items ================================== #")

letters = ["a", "b", "b", "c"]

# adding an item at the end of the list
letters.append("d")
print(letters)

# adding items at a specific position
letters.insert(0, "-")
print(letters)

# removing the item at the end of the list
letters.pop()
print(letters)

# removing an item at a specific position
letters.pop(0)
print(letters)

# removing a specific item (the code below will remove only the first 'b' from the list)
letters.remove("b")
print(letters)

# removing an item with a given input (if we have multiple 'b' then only the first one will be removed)

letters = ["e", "f", "g", "e", "f", "g"]

# delete first two items
del letters[0:2]
print(letters)

# delete all elements
letters.clear()
print(letters)


print("# ================================== Finding Items ================================== #")

letters = ["a", "b", "c", "a", "a", "a"]

# index of an object
print(letters.index("c"))

# if the object is not found in the list then it will return an error
# to handle this issue, we first check whether the object exists in the list or not
if "d" in letter:
    print(letters.index("d"))
else:
    print("Letter not found.")

# count the number of occurrences in the array
print(letters.count("a"))

print("# ================================== Sorting Lists ================================== #")

numbers = [3, 51, 2, 8, 6]

# sort the numbers in 'ascending' order
numbers.sort()
print(numbers)

# sort the numbers in 'descending' order
# the sort() method takes two parameters. 'key' and 'sort'
numbers.sort(reverse=True)
print(numbers)

print("=============================================")
numbers = [3, 51, 2, 8, 6]

# if the use sorted() method, it will return a new list that is sorted
# the old list will not be modified
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

print("=============================================")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# we cannot use the previously defined ways of sorting tuples
# we need to define a function to specify the value that will be used for sorting
# in the example below, each item will be sorted based on price


def sort_item(item):
    return item[1]


# we need specify our argument which is 'key' and set it to sort_item
items.sort(key=sort_item)
print(items)

print("# ================================== Lambda Function ================================== #")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# key=lambda
# parameter: expression
items.sort(key=lambda item: item[1])
print(items)

print("# ================================== Map Function ================================== #")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# each items in the list above is a tuple of two items
# we want to transform this list into a list of numbers
# the approach below will map the original list into a different list
prices = []
for item in items:
    prices.append(item[1])

print(prices)

print("=============================================")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# map function returns a map object which is iterable
x = map(lambda item: item[1], items)
print(x)

for item in x:
    print(item)

print("=============================================")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# we can convert the map object into a list object
prices = list(map(lambda item: item[1], items))
print(prices)

print("# ================================== Filter Function ================================== #")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# filter the price greater than or equal to 10
# the filter() will return a filter object which is iterable
# so we have to convert it into a list of objects
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

print("# ================================== List Comprehensions ================================== #")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# the functional programming approach (map)
prices = list(map(lambda item: item[1], items))
print(prices)

# the list comprehension approach ()
prices = [item[1] for item in items]
print(prices)

# the functional programming approach
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# the list comprehension approach
filtered = [item for item in items if item[1] >= 10]
print(filtered)
