import time

# Timestamp
# The code below will give us a floating point number.
# Which is the number of second from the beginning of time.
# On UNIX, this time starts from January 1st, 1970.
# We use this timestamp to perform calculations.
print(time.time())


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
