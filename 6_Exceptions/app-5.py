from time import time
from timeit import timeit


code1 = """def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(0)
except ValueError as error:
    print(error)
"""

code2 = """def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(0)
except ValueError as error:
    pass
"""

code3 = """def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("second code:", timeit(code2, number=10000))
print("third code:", timeit(code3, number=10000))
