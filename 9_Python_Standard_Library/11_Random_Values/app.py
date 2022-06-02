import random
import string

from numpy import number

# Generate random numbers between 0 to 1 (floating point)
print(random.random())

# Generate random numbers between 1 and 10
print(random.randint(1, 10))

# Takes an array and randomly picks one of the items in the array
print(random.choice([1, 2, 3, 4]))

# Returns two random items from our original array
print(random.choices([1, 2, 3, 4], k=2))

# We can generate a random password with the choices method
print(random.choices("abcdefghi", k=4))

# The code above will give us an array of random letters
# To make it a string, we do the following
print("".join(random.choices("abcdefghi", k=4)))

# If we put anything inside the empty string, it will work as a separator
# In the example below, we used comma ','
print(",".join(random.choices("abcdefghi", k=4)))

# To make the password generation more sophisticated, first we import the 'string' module
# 'string.ascii_letters' returns all the lowercase and upper case letters
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

print("".join(random.choices(string.ascii_letters + string.digits, k=6)))

# To shuffle an array, we do the following
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
