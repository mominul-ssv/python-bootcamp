from typing import final


# we use the finally clause to release external resources

# method-1
try:
    file = open("app-3.py")
    age = int(input("Age: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")
finally:
    file.close()

# method-2
# it only works for certain kinds of objects
# 'with' statement automatically release external resources
try:
    with open("app-3.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")

# open multiple files
# python will automatically the release the external resources
try:
    with open("app-3.py") as file, open("another.txt") as target:
        print("File opened.")
    age = int(input("Age: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")
