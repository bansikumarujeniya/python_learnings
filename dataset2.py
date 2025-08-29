employees = {
    1: {"name": "Alice", "age": 28, "department": "HR", "salary": 45000},
    2: {"name": "Bob", "age": 34, "department": "IT", "salary": 60000},
    3: {"name": "Charlie", "age": 29, "department": "Finance", "salary": 52000},
    4: {"name": "David", "age": 41, "department": "IT", "salary": 75000},
    5: {"name": "Eve", "age": 25, "department": "HR", "salary": 40000},
    6: {"name": "Frank", "age": 38, "department": "Marketing", "salary": 58000},
    7: {"name": "Grace", "age": 30, "department": "Finance", "salary": 55000},
    8: {"name": "Hank", "age": 33, "department": "IT", "salary": 62000},
    9: {"name": "Ivy", "age": 27, "department": "HR", "salary": 43000},
    10: {"name": "Jack", "age": 36, "department": "Sales", "salary": 57000},
    11: {"name": "Kathy", "age": 31, "department": "Finance", "salary": 54000},
    12: {"name": "Leo", "age": 39, "department": "IT", "salary": 71000},
    13: {"name": "Mona", "age": 26, "department": "Marketing", "salary": 46000},
    14: {"name": "Nick", "age": 44, "department": "Finance", "salary": 78000},
    15: {"name": "Olivia", "age": 32, "department": "HR", "salary": 50000},
    16: {"name": "Paul", "age": 29, "department": "Sales", "salary": 52000},
    17: {"name": "Quinn", "age": 35, "department": "IT", "salary": 64000},
    18: {"name": "Rita", "age": 28, "department": "Finance", "salary": 49000},
    19: {"name": "Sam", "age": 40, "department": "Marketing", "salary": 68000},
    20: {"name": "Tina", "age": 24, "department": "HR", "salary": 39000},
    21: {"name": "Uma", "age": 37, "department": "Sales", "salary": 56000},
    22: {"name": "Victor", "age": 42, "department": "IT", "salary": 77000},
    23: {"name": "Wendy", "age": 29, "department": "Finance", "salary": 51000},
    24: {"name": "Xavier", "age": 34, "department": "Marketing", "salary": 61000},
    25: {"name": "Yara", "age": 30, "department": "Sales", "salary": 53000},
    26: {"name": "Zane", "age": 45, "department": "IT", "salary": 80000},
    27: {"name": "Aiden", "age": 28, "department": "Finance", "salary": 47000},
    28: {"name": "Bella", "age": 33, "department": "HR", "salary": 52000},
    29: {"name": "Chris", "age": 39, "department": "Sales", "salary": 69000},
    30: {"name": "Diana", "age": 27, "department": "Marketing", "salary": 45000},
}

#Lists

#1. Extracting all employee names: Create a Python script that generates a list containing the names of all employees in the dataset.

employee_names = [employees[employee_id]['name'] for employee_id in employees]
print(employee_names)

#2. Filtering by age range: Write a program that takes a minimum and maximum age as input and returns a list of dictionaries for all employees within that age range.

min_age = 30
max_age = 40

employees_in_range = [
    employee for employee in employees.values()
    if min_age <= employee['age'] <= max_age
]

print(f"Employees between ages {min_age} and {max_age}:")
for employee in employees_in_range:
    print(f"- Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}")

#3. Finding all salaries: Construct a program that generates a list of all salaries from the employees dictionary.

salaries = [employee["salary"] for employee in employees.values()]
print(salaries)

#4. Employees in a department: Write a script that takes a department name as input and produces a list of all employee names in that department.

department_name = "HR"

it_employees = [
    emp['name'] for emp in employees.values()
    if emp['department'] == department_name
]

print(f"Employees in the {department_name} department:")
for name in it_employees:
    print(f"- {name}")

#5. Bonus challenge: Top 3 earners: Write a program that creates a list of the top three highest-paid employees. The items in the list should be dictionaries containing the employee's name and salary.

employee_salaries = [{"name": emp['name'], "salary": emp['salary']} for emp in employees.values()]

sorted_employees = sorted(employee_salaries, key=lambda x: x['salary'], reverse=True)

top_three_earners = sorted_employees[:3]

print("Top 3 Highest-Paid Employees:")
for employee in top_three_earners:
    print(f"- Name: {employee['name']}, Salary: {employee['salary']}")

#Tuples
#1. Immutable employee records: Create a program that converts each employee dictionary into a tuple of key-value pairs. Print the first tuple to demonstrate the conversion.

employee_records_as_tuples = []

for emp_record in employees.values():
    tuple_record = tuple(emp_record.items())
    employee_records_as_tuples.append(tuple_record)

print("Converted first employee record to a tuple of key-value pairs:")
print(employee_records_as_tuples[0])

#2.Accessing employee data: Write a script that iterates through the employees dictionary and prints a tuple for each employee, containing their name, department, and salary.

for employee_info in employees.values():
    name = employee_info['name']
    department = employee_info['department']
    salary = employee_info['salary']

    employee_tuple = (name, department, salary)
    
    print(employee_tuple)

