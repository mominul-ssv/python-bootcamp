from datetime import datetime
import time

# Custom datetime object
# datetime(Year, Month, Day)
print("# =================================== #")
dt = datetime(2022, 1, 1)
print(dt)

# This will return the current datetime
print("# =================================== #")
print(datetime.now())

# Convert a string to a datetime object
print("# =================================== #")
dt = datetime.strptime("2022/02/06", "%Y/%m/%d")
print(dt)

# Converting a timestamp to a datetime object
print("# =================================== #")
dt = datetime.fromtimestamp(time.time())
print(dt)

# Printing only year and month from a datetime object
print("# =================================== #")
print(f"{dt.year}/{dt.month}")

# Converting a datetime object to a string
print("# =================================== #")
print(dt.strftime("%Y/%m"))

# We can compare two datetime objects.
print("# =================================== #")
dt1 = datetime(2022, 1, 1)
dt2 = datetime.now()
print(dt2 > dt1)
