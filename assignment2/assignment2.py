import csv
import os
from datetime import datetime
import custom_module

# Task 2: Read a CSV File
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data
    except Exception as e:
        print("Error:", type(e).__name__, str(e))
        exit()
employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(name):
    return employees["fields"].index(name)
employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_num):
    idx = column_index("first_name")
    return employees["rows"][row_num][idx]

# Task 5: Find the Employee: a Function in a Function
def employee_find(emp_id):
    def check(row):
        return int(row[employee_id_column]) == emp_id
    return list(filter(check, employees["rows"]))

# Task 6: Find the Employee with a Lambda
def employee_find_2(emp_id):
    return list(filter(lambda r: int(r[employee_id_column]) == emp_id, employees["rows"]))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda r: r[idx])
    return employees["rows"]
sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    result = {}
    for i in range(len(employees["fields"])):
        field = employees["fields"][i]
        if field != "employee_id":
            result[field] = row[i]
    return result
print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        key = row[employee_id_column]
        result[key] = employee_dict(row)
    return result
print(all_employees_dict())

#Task 10: Use the os Module
# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11: Creating Your Own Module
def set_that_secret(value):
    custom_module.set_secret(value)
set_that_secret("my_new_secret")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_csv_file(path):
    data = {}
    rows = []

    with open(path) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                data["fields"] = row
            else:
                rows.append(tuple(row))
    data["rows"] = rows
    return data
def read_minutes():
    m1 = read_csv_file("../csv/minutes1.csv")
    m2 = read_csv_file("../csv/minutes2.csv")
    return m1, m2
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    s1 = set(minutes1["rows"])
    s2 = set(minutes2["rows"])
    return s1.union(s2)
minutes_set = create_minutes_set()

#Task 14: Convert to datetime
def create_minutes_list():
    temp = list(minutes_set)

    converted = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        temp
    ))
    return converted
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))
    with open("minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted
write_sorted_list()