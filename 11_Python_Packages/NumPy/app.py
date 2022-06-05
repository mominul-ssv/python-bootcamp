import numpy as np

# Creating a NumPy array
print("# ===============================================")
array = np.array([1, 2, 3])
print(array)

# This will return a NumPy array object
print(type(array))

# Creating a multidimensional array.
# Here, we are creating a 2D array.
# This is also known as a Matrix in math.
# We have a 2 rows, 3 columns matrix. So this is a 2 by 3 matrix.
print("# ===============================================")
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.shape)

# Creating an array with 3 rows and 4 columns and initializing each row with zero
print("# ===============================================")
array = np.zeros((3, 4))
print(array)

# Initialized the Matrix with int 0
print("# ===============================================")
array = np.zeros((3, 4), dtype=int)
print(array)

# Initialized the Matrix with int 1
print("# ===============================================")
array = np.ones((3, 4), dtype=int)
print(array)

# Initialized the Matrix with any int number
print("# ===============================================")
array = np.full((3, 4), 5, dtype=int)
print(array)

# Fill the Matrix with random numbers
print("# ===============================================")
array = np.random.random((3, 4))
print(array)

# Get an element from a Matrix / 2D array
print("# ===============================================")
print(array[0, 0])

# Getting an array of boolean value outputs
print("# ===============================================")
print(array > 0.2)

# Return only the floats that are greater than 0.2
print("# ===============================================")
print(array[array > 0.2])

# Returns the sum of all items in the 2D array
print("# ===============================================")
print(np.sum(array))

# Returns the floor of all items in the 2D array
print("# ===============================================")
print(np.floor(array))

# Returns the ceil of all items in the 2D array
print("# ===============================================")
print(np.ceil(array))

# Rounds all items in the 2D array
print("# ===============================================")
print(np.round(array))

# Arithmetic Operations
print("# ===============================================")
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)
print(first - 2)
print(first * 2)
print(first / 2)

# Convert inch to cm using NumPy
print("# ===============================================")
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)

# Convert inch to cm
dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
print(dimensions_cm)
