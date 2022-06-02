from pathlib import Path
from zipfile import ZipFile

# write
# compressing all files that exist in a folder
with ZipFile("ecommerce_files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# read
# reading compressed files
with ZipFile("ecommerce_files.zip") as zip:
    print(zip.namelist())
    print("==================================")
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
