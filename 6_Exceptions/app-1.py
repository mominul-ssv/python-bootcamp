try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
print("Execution continues.")

# using optional 'else' clause
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# printing error message
try:
    age = int(input("Age: "))
except ValueError as e:
    print("You didn't enter a valid age.")
    print(e)
    print(type(e))
print("Execution continues.")
