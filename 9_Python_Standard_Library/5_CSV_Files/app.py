import csv

from nbformat import read

# Method-1
# file = open("data.csv", "w")
# file.close()

# Method-2
# Creating and writing data to a csv file
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# reading data from a csv file
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
