from pathlib import Path

# create an absolute path object
Path("D:\\Root_Workspace\\Python_Dev")

# create an absolute path object using raw string
Path(r"D:\Root_Workspace\Python_Dev")

# crating a path object in linux or mac
Path("/user/local/bin")

# create a path object that represents the current folder
Path()

# create a path object that represents the relative path
Path("ecommerce/__init__.py")

# combine path objects together
Path() / Path("ecommerce")

# combine a path object with a string and then combine it with another string
Path() / "ecommerce" / "__init__.py"

# getting the hope directory of the current user
Path().home()

# examples
path = Path("ecommerce/__init__.py")

# check out the current directory of the defined path
print(path.absolute())

# app.py must run from the correct directory
# cd over to the directory and then run app.py
print(path.exists())

# check if it's a file
print(path.is_file())

# check if it's a directory
print(path.is_dir())

# returns the name of the file (with) extension
print(path.name)

# returns the name of the file (without) extension
print(path.stem)

# returns the extension of the file
print(path.suffix)

# returns the parent folder of the file
print(path.parent)

# create a new path object based on this existing path,
# but only change the name and the extension of the file
path = path.with_name("file.txt")
print(path)

# similar to with_name, we have with_suffix
# we use it to change the name of the extension of the file
path = path.with_name("file.py")
print(path)
