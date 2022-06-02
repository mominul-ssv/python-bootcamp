from datetime import datetime, timedelta

# dt1 = datetime(2022, 1, 1)
dt1 = datetime(2022, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()

# The code below will give us a timedelta object
duration = dt2 - dt1
print(duration)

print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())
