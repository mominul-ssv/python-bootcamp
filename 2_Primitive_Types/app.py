import math

print("# ============================================= Variables =========================================== #")

# primitive types:
# 1. strings
# 2. numbers: (int, float, complex numbers)
# 3. booleans
students_count = 1000
rating = 4.99
is_published = False

print(students_count)
print(rating)
print(is_published)

print("# ============================================= Strings =========================================== #")

course = "Python Programming"
print(course)

email = """Hi, This is Mominul. Nice to meet you."""
print(email)

print(len(course))

print("course[0] = " + course[0])  # start character of the string
print("course[-1] = " + course[-1])  # end character of the string
print("course[0:3] = " + course[0:3])
print("course[0:] = " + course[0:])
print("course[:3] = " + course[:3])
print("course[:] = " + course[:])

print("# ============================================= Escape Sequences =========================================== #")

course = "Python \"Programming\" "
print(course)

course = "Python \'Programming\' "
print(course)

course = "Python \\Programming\\ "
print(course)

course = "Python \nProgramming "
print(course)

print("# ============================================= Formatted Strings =========================================== #")

first = "Mominul"
last = "Islam"

# Using expression
# We can use any valid expression. E.g. 2 + 2, which will give us 4 in runtime.
full = f"{first} {last}"
print(full)

full = f"{len(first)} {len(last)}"
print(full)

full = f"{first} {12 + 2}"
print(full)

print("# ============================================= String Methods =========================================== #")

course = " Python programming "

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find("pro"))  # find the index of pro (first char)
print(course.replace("P", "J"))
print("Pro" in course)
print("pro" in course)
print("swift" not in course)

print("# ============================================= Numbers =========================================== #")

x = 1
x = 1.1
x = 1 + 2j  # complex number a + bi

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)   # for float
print(10 // 3)  # for int
print(10 % 3)   # modulus => remainder of a division
print(10 ** 3)  # exponent => 10 to the power of 3

x = 10
x = x + 3
x += 3  # augmented addition operator

print("# ============================================= Working with Numbers =========================================== #")

print(round(2.9))  # round the number
print(abs(-2.9))  # absolute value of a number
print(math.ceil(2.2))  # math library must be imported

x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"X: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# False
# ""
# 0
# None

# converting to boolean
# >>> bool(0)
# >>> False

# >>> bool(1)
# >>> True

# >>> bool(-1)
# >>> True

# >>> bool(5)
# >>> True

# empty string return false
# >>> bool("")
# >>> False

# >>> bool("Test")
# >>> True
