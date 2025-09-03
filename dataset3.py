employee_data = {
    'employee_id': [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130
    ],
    'first_name': [
        'Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Charlotte', 'Elijah', 'Amelia', 'James', 'Ava',
        'William', 'Sophia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Theodore', 'Harper',
        'Daniel', 'Madison', 'Jacob', 'Scarlett', 'Michael', 'Victoria', 'Alexander', 'Luna', 'Sebastian', 'Penelope'
    ],
    'last_name': [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
        'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
        'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King'
    ],
    'department': [
        'Marketing', 'Sales', 'Engineering', 'Marketing', 'IT', 'Sales', 'IT', 'Marketing', 'Engineering', 'HR',
        'Sales', 'Engineering', 'IT', 'HR', 'Marketing', 'Sales', 'IT', 'HR', 'Engineering', 'Marketing',
        'Sales', 'IT', 'Engineering', 'HR', 'Sales', 'Marketing', 'Engineering', 'IT', 'Sales', 'HR'
    ],
    'hire_date': [
        '2022-01-15', '2021-05-20', '2023-03-10', '2022-08-01', '2021-11-25', '2022-06-30', '2023-01-05', '2022-04-12',
        '2023-07-18', '2022-09-22',
        '2021-08-10', '2023-02-28', '2022-03-19', '2021-09-01', '2023-05-14', '2022-07-07', '2023-08-21', '2021-10-17',
        '2022-12-05', '2023-04-25',
        '2021-06-03', '2022-02-14', '2023-06-11', '2021-12-28', '2023-09-02', '2022-11-08', '2021-07-26', '2023-03-30',
        '2022-05-09', '2023-01-20'
    ],
    'salary': [
        75000, 82000, 95000, 78000, 85000, 81000, 92000, 76000, 98000, 70000,
        83000, 96000, 88000, 72000, 79000, 80000, 91000, 74000, 97000, 77000,
        84000, 89000, 94000, 71000, 86000, 78000, 93000, 90000, 87000, 73000
    ],
    'job_title': [
        'Marketing Specialist', 'Sales Representative', 'Software Engineer', 'Marketing Coordinator',
        'IT Support Specialist', 'Sales Manager', 'IT Analyst', 'Marketing Specialist', 'Lead Engineer',
        'HR Coordinator',
        'Sales Representative', 'Senior Software Engineer', 'IT Project Manager', 'Recruiter', 'Marketing Analyst',
        'Sales Representative', 'Systems Administrator', 'HR Manager', 'Software Engineer', 'Marketing Manager',
        'Sales Manager', 'Network Engineer', 'Product Manager', 'HR Generalist', 'Sales Representative',
        'Marketing Coordinator', 'Data Scientist', 'IT Specialist', 'Sales Manager', 'Payroll Specialist'
    ],
    'performance_rating': [
        'Exceeds Expectations', 'Fully Meets', 'Exceeds Expectations', 'Fully Meets', 'Needs Improvement',
        'Fully Meets', 'Fully Meets', 'Fully Meets', 'Exceeds Expectations', 'Fully Meets',
        'Fully Meets', 'Exceeds Expectations', 'Fully Meets', 'Needs Improvement', 'Fully Meets', 'Fully Meets',
        'Fully Meets', 'Exceeds Expectations', 'Exceeds Expectations', 'Fully Meets',
        'Fully Meets', 'Fully Meets', 'Exceeds Expectations', 'Fully Meets', 'Fully Meets', 'Fully Meets',
        'Exceeds Expectations', 'Fully Meets', 'Fully Meets', 'Fully Meets'
    ],
    'years_of_experience': [
        3, 4, 2, 3, 4, 3, 2, 3, 2, 3,
        4, 2, 3, 4, 2, 3, 2, 4, 3, 2,
        4, 3, 2, 4, 2, 3, 4, 2, 3, 4
    ],
    'location': [
        'New York', 'Boston', 'San Francisco', 'New York', 'Chicago', 'Boston', 'San Francisco', 'New York',
        'San Francisco', 'Boston',
        'Chicago', 'San Francisco', 'Chicago', 'Boston', 'New York', 'Boston', 'Chicago', 'New York', 'San Francisco',
        'New York',
        'Boston', 'Chicago', 'San Francisco', 'New York', 'Chicago', 'Boston', 'San Francisco', 'Chicago', 'Boston',
        'New York'
    ],
    'employment_status': [
        'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active',
        'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active',
        'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active'
    ]
}

#Lists
#1. What is the first_name of the employee at index 5 in the employee_data dictionary?
employee_name = employee_data['first_name'][5]
print(employee_name)

#2. How many employees are in the employee_id list?
employee_id_list = employee_data['employee_id']
number_of_employees = len(employee_id_list)
print(number_of_employees)

#3. Write a function to find and print the first_name and last_name of all employees with a performance_rating of 'Exceeds Expectations'.
def find_employees_with_exceeds_expectations(data):

    print("Employees with 'Exceeds Expectations' rating:")
    found_employees = 0

    for first_name, last_name, performance in zip(data['first_name'], data['last_name'], data['performance_rating']):
        if performance == 'Exceeds Expectations':
            print(f"- {first_name} {last_name}")
            found_employees += 1

    if found_employees == 0:
        print("No employees with 'Exceeds Expectations' rating.")

find_employees_with_exceeds_expectations(employee_data)

#4. Write a function that takes a department name as an argument and returns a list of all employee_ids in that department.
def get_employee_ids_by_department(data, department_name):

    employee_ids = []
    for emp_id, dept in zip(data['employee_id'], data['department']):
        if dept == department_name:
            employee_ids.append(emp_id)
    return employee_ids

sales_employees = get_employee_ids_by_department(employee_data, 'Sales')
print(f"Employee IDs in the 'Sales' department: {sales_employees}")

hr_employees = get_employee_ids_by_department(employee_data, 'HR')
print(f"Employee IDs in the 'HR' department: {hr_employees}")

it_employees = get_employee_ids_by_department(employee_data, 'IT')
print(f"Employee IDs in the 'IT' department: {it_employees}")

#5. Create a new list of tuples, where each tuple contains the first_name, department, and salary for employees with a salary greater than 90000.
def get_high_earner_info(data):

    high_earner_list = []

    for first_name, department, salary in zip(data['first_name'], data['department'], data['salary']):
        if salary > 90000:
            high_earner_list.append((first_name, department, salary))
    return high_earner_list

high_earners = get_high_earner_info(employee_data)

print("Employees with a salary greater than 90,000:")
for employee_tuple in high_earners:
    print(employee_tuple)


#Dictionary
#1. Access and print the list of last_names from the employee_data dictionary.

last_names_list = employee_data['last_name']
print(f"The list of last names is: {last_names_list}")

#2. Check if the key 'performance_rating' exists in the employee_data dictionary.

key = 'performance_rating'

if key in employee_data:
    print(f"The key '{key}' exists")
else:
    print(f"The key '{key}' does not exist")

#3. Create a new dictionary that maps each employee_id to their department.

employee_dept_map = dict(zip(employee_data['employee_id'], employee_data['department']))

print("Employee ID to Department Map:")
print(employee_dept_map)

#4. Count and print how many employees are in each department and store the result in a new dictionary.

department_counts = {}

for department in employee_data['department']:
    if department in department_counts:
        department_counts[department] += 1
    else:
        department_counts[department] = 1

print("Employee count by department:")
print(department_counts)

#5. Restructure the employee_data into a new dictionary where each key is an employee_id, and its value is another dictionary containing all the other employee details (first_name,last_name, etc.).

keys = [key for key in employee_data.keys() if key != 'employee_id']
restructured_data = {}

for emp_id, values in zip(employee_data['employee_id'], zip(*(employee_data[key] for key in keys))):
    employee_details = {key: value for key, value in zip(keys, values)}
    restructured_data[emp_id] = employee_details

import json
print(json.dumps(restructured_data, indent=4))

#Tuple
#1. What is the salary of the employee at index 10? Access this value from the dictionary and print it.

salaries = employee_data['salary']
salary_at_index_10 = salaries[10]
print(salary_at_index_10)

#2. Print a tuple containing the first_name and last_name of the employee with employee_id 105.

try:
    index_105 = employee_data['employee_id'].index(105)

    first_name_105 = employee_data['first_name'][index_105]
    last_name_105 = employee_data['last_name'][index_105]

    employee_tuple = (first_name_105, last_name_105)

    print(f"The first name and last name of employee 105 are: {employee_tuple}")

except ValueError:
    print("Employee ID 105 not found in the dataset.")

#3. Use the zip() function to create a list of tuples, where each tuple contains an employee_id, first_name, and department. Print the resulting list.

employee_info_list = list(zip(employee_data['employee_id'], employee_data['first_name'], employee_data['department']))

print("List of employee tuples (ID, First Name, Department):")
for employee_tuple in employee_info_list:
    print(employee_tuple)

#4. Write a program to count the number of employees who have a performance_rating of 'Fully Meets' and years_of_experience of 3 using tuples.
def count_fully_meets_with_3_years(data):
    count = 0

    for rating, experience in zip(data['performance_rating'], data['years_of_experience']):
        if rating == 'Fully Meets' and experience == 3:
            count += 1
    return count

employees_with_specific_criteria = count_fully_meets_with_3_years(employee_data)
print(f"Number of employees with 'Fully Meets' rating and 3 years experience: {employees_with_specific_criteria}")

#5. Create a list of tuples where each tuple contains a department, the number of employees in that department, and the average salary for that department. Sort the list of tuples based on the average salary in descending order.
from collections import defaultdict

def analyze_departments(data):
    department_salaries = defaultdict(list)
    for department, salary in zip(data['department'], data['salary']):
        department_salaries[department].append(salary)

    department_stats = []
    for department, salaries in department_salaries.items():
        num_employees = len(salaries)
        average_salary = sum(salaries) / num_employees
        department_stats.append((department, num_employees, average_salary))

    sorted_stats = sorted(department_stats, key=lambda x: x[2], reverse=True)

    return sorted_stats

department_summary = analyze_departments(employee_data)
print("Department statistics, sorted by average salary (descending):")
for item in department_summary:
    department, count, avg_salary = item
    print(f"Department: {department}, Employees: {count}, Average Salary: {avg_salary:.2f}")


#Class and Objects
#1. Define a class Employee with attributes for first_name and last_name. Create an instance of this class for the first employee in the dataset.
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

first_employee_first_name = employee_data['first_name'][0]
first_employee_last_name = employee_data['last_name'][0]

first_employee = Employee(first_employee_first_name, first_employee_last_name)
print(f"First employee instance created with name: {first_employee.first_name} {first_employee.last_name}")

#2. Create an object for the employee with employee_id 110 and print their first_name.
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

try:
    employee_index = employee_data['employee_id'].index(110)

    target_first_name = employee_data['first_name'][employee_index]
    target_last_name = employee_data['last_name'][employee_index]

    employee_110 = Employee(target_first_name, target_last_name)
    print(f"First name of employee with ID 110: {employee_110.first_name}")

except ValueError:
    print("Employee with ID 110 not found.")

#3. Modify the Employee class to include all attributes from the employee_data dictionary (employee_id, first_name, last_name, department, salary, job_title, performance_rating, years_of_experience, location, employment_status).
class Employee:

    def __init__(self, employee_id, first_name, last_name, department, hire_date,
                 salary, job_title, performance_rating, years_of_experience,
                 location, employment_status):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.hire_date = hire_date
        self.salary = salary
        self.job_title = job_title
        self.performance_rating = performance_rating
        self.years_of_experience = years_of_experience
        self.location = location
        self.employment_status = employment_status


try:
    employee_index = employee_data['employee_id'].index(113)
    employee_113_data = {key: employee_data[key][employee_index] for key in employee_data}
    employee_113 = Employee(**employee_113_data)

    print(f"First name of employee with ID 113: {employee_113.first_name}")
    print(f"Job title of employee with ID 113: {employee_113.job_title}")

except ValueError:
    print("Employee with ID 113 not found.")

#4. Write a method in the Employee class called get_salary_info() that prints a message like "Liam Smith earns 75000 and has a performance rating of 'Exceeds Expectations'".
class Employee:

    def __init__(self, employee_id, first_name, last_name, department, hire_date,
                 salary, job_title, performance_rating, years_of_experience,
                 location, employment_status):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.hire_date = hire_date
        self.salary = salary
        self.job_title = job_title
        self.performance_rating = performance_rating
        self.years_of_experience = years_of_experience
        self.location = location
        self.employment_status = employment_status

    def get_salary_info(self):
        print(
            f"{self.first_name} {self.last_name} earns {self.salary} and has a performance rating of '{self.performance_rating}'")

try:
    employee_index = employee_data['employee_id'].index(110)

    employee_110_data = {key: employee_data[key][employee_index] for key in employee_data}

    employee_110 = Employee(**employee_110_data)

    employee_110.get_salary_info()

    first_employee_data = {key: employee_data[key][0] for key in employee_data}
    first_employee = Employee(**first_employee_data)
    first_employee.get_salary_info()

except ValueError:
    print("Employee with ID 110 not found.")

#5. Create a class Department with attributes for name and a list of employees. Write a program to instantiate Department objects for each unique department and populate their employee lists using the provided data.
class Employee:
    def __init__(self, employee_id, first_name, last_name, department, hire_date, salary, job_title, performance_rating,
                 years_of_experience, location, employment_status):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.hire_date = hire_date
        self.salary = salary
        self.job_title = job_title
        self.performance_rating = performance_rating
        self.years_of_experience = years_of_experience
        self.location = location
        self.employment_status = employment_status

    def __repr__(self):
        return f"Employee(name='{self.first_name} {self.last_name}', department='{self.department}')"

class Department:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise TypeError("Only Employee objects can be added to a department.")

    def __repr__(self):
        return f"Department(name='{self.name}')"

if __name__ == "__main__":
    departments = {}
    number_of_employees = len(employee_data['employee_id'])

    for i in range(number_of_employees):
        employee_id = employee_data['employee_id'][i]
        first_name = employee_data['first_name'][i]
        last_name = employee_data['last_name'][i]
        department_name = employee_data['department'][i]
        hire_date = employee_data['hire_date'][i]
        salary = employee_data['salary'][i]
        job_title = employee_data['job_title'][i]
        performance_rating = employee_data['performance_rating'][i]
        years_of_experience = employee_data['years_of_experience'][i]
        location = employee_data['location'][i]
        employment_status = employee_data['employment_status'][i]


        employee = Employee(
            employee_id, first_name, last_name, department_name, hire_date,
            salary, job_title, performance_rating, years_of_experience,
            location, employment_status
        )

        if department_name not in departments:
            departments[department_name] = Department(department_name)

        departments[department_name].add_employee(employee)

    print("Populated Departments:")
    for department_name, department_object in departments.items():
        print(f"\n--- Department: {department_name} ---")
        print("Employees:")
        for employee in department_object.employees:
            print(f"  - {employee.first_name} {employee.last_name} ({employee.job_title})")































































































