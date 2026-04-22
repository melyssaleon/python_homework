# Task 3: List Comprehensions Practice
import csv
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
names = [
    row[0] + " " + row[1]
    for row in data[1:]
]
print(names)
names_with_e = [
    name for name in names
    if "e" in name.lower()
]
print(names_with_e)