# method-1
try:
    age = int(input("Age: "))
    xFactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("You didn't enter a valid age.")
print("Execution continues.")

# method-2
try:
    age = int(input("Age: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
print("Execution continues.")
