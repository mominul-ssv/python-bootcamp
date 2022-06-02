from pathlib import Path
from time import ctime
import shutil

from sympy import source

path = Path("ecommerce/__init__.py")

# Check if the file exists or not
# path.exists()

# Rename the file
# path.rename("init.txt")

# Delete a file
# path.unlink()

# Returns information about the file
path.stat()

# This will return a stat result object.
# For example: 'st_size' returns the size of this object in bytes.
# For example: 'st_atime' returns the last access time.
# For example: 'st_mtime' returns the last modified time.
# For example: 'st_ctime' returns the creation time.
print("# ======================= #")
print(path.stat())

# To covert 'epic' time to human readable time, we need to import 'ctime' from the 'time' module
print("# ======================= #")
print(ctime(path.stat().st_ctime))

# Returns the content of the file as a bytes object for representing binary data
print("# ======================= #")
print(path.read_bytes())

# Returns the content of the file as a string
print("# ======================= #")
print(path.read_text())

# Using the method above is easier than the built-in open() function.
# Because once we use the open() function, we must also close it.
# ===============================================================
# file = open("__init__.py", "r")

# If we use the 'with' statement, it automatically gets closed.
# =============================================================
# with open("__init__.py", "r") as file:
#     pass

# **Note: So, using read_text() method is a much better option.

# Write textual data to a file
# Open the file pointed to in text mode, write data to it, and close the file
# ===========================================================================
# path.write_text("...")

# Open the file pointed to in bytes mode, write data to it, and close the file
# ============================================================================
# path.write_bytes("...")

# Copying files using 'path' object is possible but not the ideal choice
# To write file using Path object, we do the following
# ====================================================
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())

# Alternatively, we can use a module call shutil
# ==============================================
# shutil.copy(source, target)
