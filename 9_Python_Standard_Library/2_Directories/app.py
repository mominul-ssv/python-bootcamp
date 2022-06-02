from pathlib import Path

path = Path("ecommerce")

# Check if the directory exists or not
# path.exists()

# Crate the directory
# path.mkdir()

# Remove the directory
# path.rmdir()

# Rename the directory to a new name
# path.rename("ecommerce2")

# We can get the list of files and directories in this path
# path.iterdir()

# This will return a generator object.
# A generator object returns a new value every time we iterate it.
# So when we are storing a large list of items, we use generator object.
# Because it doesn't save all the generated output in the memory.
# It returns a new generator object in each iteration.
print(path.iterdir())

# 'app.py' must run from the correct directory
# 'cd' over to the directory and then run app.py
print("# ======================= #")
for p in path.iterdir():
    print(p)

print("# ======================= #")
paths = [p for p in path.iterdir()]
print(paths)

print("# ======================= #")
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# The method above is very useful if we want to get the list of files and directories in a path.
# But it has two limitations.
# 1. We cannot search by a pattern
# 2. It doesn't search recursively
# To overcome this issue, we use 'glob'
print("# ======================= #")
paths = [p for p in path.iterdir() if p.is_dir()]

# This will give us only the '.py' files
# This also returns a generator
py_files = path.glob("*.py")
print(py_files)

py_files = [p for p in path.glob("*.py")]
print(py_files)

# To search recursively, we use the following technique
print("# ======================= #")
py_files = [p for p in path.glob("**/*.py")]
print(py_files)

# We can also use 'rglob'
# The following code returns all the .py files in the ecommerce directory and all its children
print("# ======================= #")
py_files = [p for p in path.rglob("*.py")]
print(py_files)
