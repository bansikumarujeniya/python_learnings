employees_data = {
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
'''
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

#2. Accessing employee data: Write a script that iterates through the employees dictionary and prints a tuple for each employee, containing their name, department, and salary.

for employee_info in employees.values():
    name = employee_info['name']
    department = employee_info['department']
    salary = employee_info['salary']

    employee_tuple = (name, department, salary)
    
    print(employee_tuple)

#3. Comparing data structures: Based on the employees data, provide an example of when using a tuple is preferable to a list.

employee_record = ("Alice", 28, "HR", 45000)

try:
    employee_record[1] = 29
except TypeError as e:
    print(f"Error: {e}")

#4. Handling nested data: Write a program that, for each department, creates a tuple containing the department name and a list of employee names within it. Print the tuple for the 'IT' department.

department_employees = {}

for emp_id, data in employees.items():
    department = data['department']
    name = data['name']

    if department not in department_employees:
        department_employees[department] = [name]
    else:
        department_employees[department].append(name)

it_department_tuple = (
    'IT',
    department_employees['IT']
)

print(f"IT Department Tuple: {it_department_tuple}")

#5. Bonus challenge: Aggregating department data: Write a function that returns a list of tuples. Each tuple should contain a department's name and the total salary of its employees.

def get_department_salaries(employees_data):

    department_salaries = {}

    for employee in employees_data.values():
        department = employee['department']
        salary = employee['salary']
        department_salaries[department] = department_salaries.get(department,0) + salary

    return list(department_salaries.items())

department_salary_list = get_department_salaries(employees)
print(department_salary_list)

#Dictionary
#1. Updating employee information: Write a script to increase the salary of all employees in the 'HR' department by 10%. Print the updated dictionary entry for 'Bella' to confirm the change.

for employee_id, employee_info in employees.items():
    if employee_info['department'] == 'HR':
        employee_info['salary'] *= 1.1

for employee_id, employee_info in employees.items():
    if employee_info['name'] == 'Bella':
        print(f"Updated entry for Bella: {employee_info}")
        break

#2. Counting employees per department: Create a program that generates a new dictionary where each key is a department name and the corresponding value is the number of employees in that department.

def count_employees_per_department(employees_data):

    department_counts = {}

    for employee_id, employee_info in employees_data.items():
        department = employee_info['department']

        if department in department_counts:
            department_counts[department] += 1
        else:
            department_counts[department] = 1

    return department_counts

employee_counts_by_department = count_employees_per_department(employees)
print(employee_counts_by_department)

#3. Filtering by salary and department: Write a program that creates a new dictionary containing only the employees from the 'Finance' department who earn more than $50,000.

finance_high_earners = {}

for employee_id, employee_data in employees.items():
    is_finance = employee_data.get("department") == "Finance"
    is_high_earner = employee_data.get("salary") > 50000

    if is_finance and is_high_earner:
        finance_high_earners[employee_id] = employee_data

print(finance_high_earners)

#4. Creating nested dictionaries: Write a script that restructures the data into a nested dictionary where department names are the keys. Each value should be a dictionary of employees within that department, using employee names as keys.

departments_nested = {}

for employee_id, employee_data in employees.items():
    department = employee_data.get("department")
    employee_name = employee_data.get("name")

    employee_data.pop("department", None)
    employee_data.pop("name", None)

    if department not in departments_nested:
        departments_nested[department] = {}

    departments_nested[department][employee_name] = employee_data

import json
print(json.dumps(departments_nested, indent=4))

#5. Bonus challenge: Merging data: Assume you have a second dictionary of employee IDs and job titles. Write a program to merge this new information into the employees dictionary.

job_titles = {
    1: "HR Specialist",
    2: "Software Developer",
    3: "Financial Analyst",
    4: "Senior Software Developer",
    5: "HR Coordinator",
    6: "Marketing Manager",
    7: "Financial Analyst",
    8: "IT Support Specialist",
    9: "HR Specialist",
    10: "Sales Representative",
    11: "Financial Analyst",
    12: "Network Engineer",
    13: "Marketing Assistant",
    14: "Senior Financial Analyst",
    15: "HR Manager",
    16: "Sales Representative",
    17: "Systems Analyst",
    18: "Financial Clerk",
    19: "Marketing Specialist",
    20: "HR Intern",
    21: "Sales Manager",
    22: "IT Manager",
    23: "Financial Analyst",
    24: "Marketing Specialist",
    25: "Sales Representative",
    26: "IT Director",
    27: "Financial Analyst",
    28: "HR Generalist",
    29: "Sales Director",
    30: "Marketing Coordinator",
}

for emp_id, title in job_titles.items():
    if emp_id in employees:
        employees[emp_id]['job_title'] = title

print("Updated entry for Alice (ID 1):", employees[1])
print("Updated entry for Bob (ID 2):", employees[2])
print("Updated entry for Bella (ID 28):", employees[28])
print("Updated entry for Chris (ID 29):", employees[29])
print("Updated entry for Diana (ID 30):", employees[30])
'''
#Class and Objects
#1. Defining an Employee class: Create a class named Employee that initializes with attributes for an employee's ID, name, age, department, and salary.

class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def __repr__(self):
        return (f"Employee(id={self.id}, name='{self.name}', age={self.age}, "
                f"department='{self.department}', salary={self.salary})")

employee_objects = []

for emp_id, data in employees_data.items():
    employee_objects.append(
        Employee(
            emp_id=emp_id,
            name=data["name"],
            age=data["age"],
            department=data["department"],
            salary=data["salary"]
        )
    )

print("dataset:")
for i in range(3):
    print(employee_objects[i])

alice_object = employee_objects[0]
print("\nAccessing attributes of Alice:")
print(f"Name: {alice_object.name}")
print(f"Salary: {alice_object.salary}")

#2. Creating a Company class: Create a Company class that takes the employees dictionary as an attribute during initialization.

class Company:
    def __init__(self, employees_data):
        self.employees = employees_data

    def __repr__(self):
        return f"Company with {len(self.employees)} employees."


my_company = Company(employees_data)
print(my_company)

print("\nAccessing employees from the Company object:")
print(my_company.employees[1])

#3. Implementing a method for a Company object: Add a method to the Company class called get_avg_salary_by_department(department_name) that calculates and returns the average salary for a given department.

class Company:
    def __init__(self, employees_data):
        self.employees = employees_data

    def get_avg_salary_by_department(self, department_name):

        salaries = []
        for employee_data in self.employees.values():
            if employee_data["department"] == department_name:
                salaries.append(employee_data["salary"])

        if salaries:
            return sum(salaries) / len(salaries)
        else:
            return 0

    def __repr__(self):
        return f"Company with {len(self.employees)} employees."


my_company = Company(employees_data)

avg_salary_it = my_company.get_avg_salary_by_department("IT")
avg_salary_hr = my_company.get_avg_salary_by_department("HR")
avg_salary_sales = my_company.get_avg_salary_by_department("Sales")
avg_salary_nonexistent = my_company.get_avg_salary_by_department("R&D")

print(f"Average salary for IT department: {avg_salary_it:,.2f}")
print(f"Average salary for HR department: {avg_salary_hr:,.2f}")
print(f"Average salary for Sales department: {avg_salary_sales:,.2f}")
print(f"Average salary for R&D department: {avg_salary_nonexistent:,.2f}")

#4. Representing employees as objects: Write a script that creates a list of Employee objects from the employees dictionary.

employee_objects = []

for emp_id, data in employees_data.items():
    employee_objects.append(
        Employee(
            emp_id=emp_id,
            name=data["name"],
            age=data["age"],
            department=data["department"],
            salary=data["salary"]
        )
    )

print("List of all employee objects:")
print(employee_objects)
print("\nFirst three employee objects in the list:")
for emp in employee_objects[:3]:
    print(emp)

#5. Bonus challenge: Employee management system: (1) Create a method within the Company class called promote_employee(employee_id, new_salary) that updates an employee's salary based on their ID.(2) Test the method by promoting the employee with ID 2 to a new salary of $65,000 and printing their updated details.

class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def __repr__(self):
        return (f"Employee(id={self.id}, name='{self.name}', age={self.age}, "
                f"department='{self.department}', salary={self.salary})")


class Company:
    def __init__(self, employees_data):
        self.employees = employees_data

    def get_avg_salary_by_department(self, department_name):
        salaries = []
        for employee_data in self.employees.values():
            if employee_data["department"] == department_name:
                salaries.append(employee_data["salary"])

        if salaries:
            return sum(salaries) / len(salaries)
        else:
            return 0

    def promote_employee(self, employee_id, new_salary):
        if employee_id in self.employees:
            self.employees[employee_id]["salary"] = new_salary
            print(f"Employee {employee_id} has been promoted. New salary: {new_salary:,.2f}")
        else:
            print(f"Error: Employee with ID {employee_id} not found.")

    def __repr__(self):
        return f"Company with {len(self.employees)} employees."

my_company = Company(employees_data)

employee_id_to_promote = 2
print("Original details of Employee 2 (Bob):")
print(my_company.employees.get(employee_id_to_promote))

my_company.promote_employee(employee_id=employee_id_to_promote, new_salary=65000)

print("\nUpdated details of Employee 2 (Bob):")
print(my_company.employees.get(employee_id_to_promote))

my_company.promote_employee(employee_id=99, new_salary=100000)
my_company.promote_employee(employee_id=30, new_salary=60000)
