import sys

# argv = argument variables
print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
