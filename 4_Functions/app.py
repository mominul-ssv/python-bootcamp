# There are two types of functions:
# 1 - A function that perform a task
# 2 - A function that calculate and return a value

print("# ================================== Type - 1 ================================== #")


def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Mominul", "Islam")

# first_name -> parameter
# Mominul -> argument

print("# ================================== Type - 2 ================================== #")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John Smith")
print(message)

# file = open("content.txt", "w")
# file.write(message)

# def greet(name)
#     print(f"Hi {name}")
#
# print(greet("Mosh"))
#
# **Note: We will get 'None' as an output. Because in Python, all functions by default returns 'None' value.
#         If we specify a return statement then and only then 'None' gets replaced by the return value.

print("# ================================== Keyword Arguments ================================== #")


def increment(number, by):
    return number + by


# use keyword arguments to make code more readable
print(increment(2, 1))
print(increment(2, by=1))

print("# ================================== Default Arguments ================================== #")


def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 5))

# all optional parameters like 'by=1' must come after the required parameters. (num1, num2, by=1)

print("# ================================== xargs ================================== #")

# this code will create a tuple of objects (2, 3, 4, 5)
# list: [2, 3, 4, 5]
# tuple: (2, 3, 4, 5)


def multiply(*numbers):
    sum = 1
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return sum, product


# show both sum & product
print(multiply(2, 3, 4, 5))

# show only sum
print(multiply(2, 3, 4, 5)[0])

# show only product
print(multiply(2, 3, 4, 5)[1])

print("# ================================== xxargs ================================== #")

# key-value pairs
# the object below is known as dictionary


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="John", age=22)


print("# ================================== Scope ================================== #")

# discussion on local variables & global variables
# bad practice and must be avoided at all cost


message = "a"


def greet():
    global message
    message = "b"


greet()
print(message)

print("# ================================== Debugging ================================== #")

# create an indentation bug at line 137 to view the debugging


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiply(5, 10, 2))


print("# ================================== Exercise ================================== #")


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(7))
