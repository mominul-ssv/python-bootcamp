from itertools import count
from click import command


print("# ============================================= Comparison Operator =========================================== #")

# 10 > 3
# 10 >= 3
# 10 < 20
# 10 <= 20
# 10 == 10
# 10 == "10"
# 10 != "10"
print(10 == "10")

print("# ============================================= Conditional Statements =========================================== #")

temp = 25
if temp > 30:
    print("It's warm")
    print("Drink water")
elif temp > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

print("# ============================================= Ternary Operator =========================================== #")

# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

print("# ============================================= Logical Operators =========================================== #")

high_income = True
good_credit = False
student = True

# 'and' operator
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# 'or' operator
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# 'not' operator
if not student:
    print("Eligible")
else:
    print("Not eligible")

# combination of logical operators (logical operators are short-circuit)
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# chaining comparison operators
# if age >=18 and age < 65:
# if 18 <= age < 65:
age = 22
if 18 <= age < 65:
    print("Eligible")

# quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

print("# ============================================= For Loops =========================================== #")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Test", number, (number) * ".")

# here, 2 is the increment step 0 -> 2 -> 4
for number in range(0, 10, 2):
    print("Step", number, (number) * ".")

print("# ============================================= For..Else =========================================== #")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed!")

# here, the else block of code will only execute if the 'for' loop do not break

print("# ============================================= Nested Loops =========================================== #")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print("# ============================================= Iterables =========================================== #")

print(type(5))  # primitive type
print(type(range(5)))  # complex type

# iterable (range)
for x in range(3):
    print(x)

# iterable (string)
for x in "Python":
    print(x)

# iterable (list)
for x in [11, 22, 33, 44]:
    print(x)

# iterable (custom objects)
# will be shown later

print("# ============================================= While Loops =========================================== #")

number = 100
while number > 0:
    print(number)
    number = number // 2  # number /= 2

inputCommand = ""
while inputCommand.lower() != "quit":
    inputCommand = input(">")
    print("ECHO", inputCommand)

# handing infinite loops
while True:
    inputCommand = input(">")
    print("ECHO", command)
    if inputCommand.lower() == "quit":
        break

print("# ============================================= Exercise =========================================== #")
count = 0

for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
