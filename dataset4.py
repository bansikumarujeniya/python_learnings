employee_data = [
    {"id": 1, "name": "Amber Peterson", "email": "cwilson@example.net", "job_title": "Editor, commissioning",
     "company": "Smith, Mcdonald and Hernandez", "address": "7616 Amanda Inlet\nEast William, OR 07705",
     "last_login": "2020-03-24"},
    {"id": 2, "name": "Jason Anderson", "email": "kellyrobert@example.org", "job_title": "Occupational psychologist",
     "company": "Johnson, Rodriguez and Fisher", "address": "PSC 6323, Box 6006\nAPO AP 40228",
     "last_login": "2024-03-10"},
    {"id": 3, "name": "Timothy Evans", "email": "wthompson@example.net", "job_title": "Pharmacist",
     "company": "Sanchez, Rodriguez and Diaz", "address": "298 Sanchez Drive\nSouth Angelamouth, NH 69652",
     "last_login": "2022-10-18"},
    {"id": 4, "name": "Mr. Jesse Ramirez", "email": "karl16@example.com",
     "job_title": "IT technical support professional", "company": "White, Ramirez and Jones",
     "address": "813 James Path\nSouth Annaburgh, UT 27329", "last_login": "2021-08-01"},
    {"id": 5, "name": "Mary Hall", "email": "christine91@example.org", "job_title": "Physiotherapist",
     "company": "Lee Group", "address": "3391 David Stream Suite 357\nEast Stephenfurt, IL 42967",
     "last_login": "2020-11-20"},
    {"id": 6, "name": "Scott Miller", "email": "kellermeredith@example.com", "job_title": "Air cabin crew",
     "company": "Turner PLC", "address": "8064 Anderson Stream Apt. 367\nNorth Michaelmouth, CO 95537",
     "last_login": "2020-01-20"},
    {"id": 7, "name": "Lisa Morgan", "email": "jessica97@example.com", "job_title": "Conservation officer",
     "company": "Hernandez-Lopez", "address": "76159 Scott Plaza Suite 837\nSouth Jamesbury, MI 49959",
     "last_login": "2024-08-25"},
    {"id": 8, "name": "Mary Torres", "email": "kenneth47@example.net", "job_title": "Museum education officer",
     "company": "Russell and Sons", "address": "28358 Michael Inlet\nNorth Crystal, SC 60925",
     "last_login": "2024-03-24"},
    {"id": 9, "name": "Jeffrey Thomas", "email": "wturner@example.net", "job_title": "Scientist, water quality",
     "company": "Brown-Johnson", "address": "97029 Lisa Port Apt. 522\nEast Kevin, OK 22444",
     "last_login": "2024-08-08"},
    {"id": 10, "name": "Ashley Hill", "email": "lisa45@example.org", "job_title": "Retail merchandiser",
     "company": "Baker, Wilson and Lee", "address": "4092 Williams Flat Suite 350\nNorth James, OK 16867",
     "last_login": "2022-09-24"},
    {"id": 11, "name": "Christopher Lopez", "email": "dianabrown@example.net", "job_title": "Production manager",
     "company": "Jones-Thompson", "address": "908 Stephanie Creek\nWest Jessicaville, ND 71754",
     "last_login": "2024-09-02"},
    {"id": 12, "name": "Lisa Harris", "email": "garciakelly@example.org", "job_title": "Advertising account executive",
     "company": "Peterson-Hernandez", "address": "15370 Thomas Walk\nWest Christopher, HI 75787",
     "last_login": "2023-01-20"},
    {"id": 13, "name": "David Ramirez", "email": "johnnelson@example.net", "job_title": "Advertising account executive",
     "company": "Smith, Mcdonald and Hernandez", "address": "66481 Russell Islands\nSouth Johnport, PA 35326",
     "last_login": "2023-10-21"},
    {"id": 14, "name": "Richard Garcia", "email": "hickskatherine@example.org", "job_title": "Horticultural consultant",
     "company": "Johnson, Rodriguez and Fisher", "address": "76949 Amy Pike Suite 174\nMartinezland, WV 96627",
     "last_login": "2024-06-03"},
    {"id": 15, "name": "Matthew Hernandez", "email": "robert84@example.com", "job_title": "Air cabin crew",
     "company": "Sanchez, Rodriguez and Diaz", "address": "298 Jessica Valley\nEast Joseph, AR 13190",
     "last_login": "2021-02-13"},
    {"id": 16, "name": "Joseph Smith", "email": "christopher36@example.org", "job_title": "Building surveyor",
     "company": "White, Ramirez and Jones", "address": "9935 Anthony Stream Apt. 182\nSouth Anthonychester, IN 67676",
     "last_login": "2021-05-19"},
    {"id": 17, "name": "Michael Davis", "email": "jessica82@example.org", "job_title": "Social researcher",
     "company": "Lee Group", "address": "7567 James Drive\nLake Jessicaborough, WY 91873", "last_login": "2024-07-28"},
    {"id": 18, "name": "Lisa Morgan", "email": "mark27@example.org", "job_title": "Retail merchandiser",
     "company": "Turner PLC", "address": "733 Ryan Alley\nWest Elizabethhaven, SC 76953", "last_login": "2024-02-15"},
    {"id": 19, "name": "Lisa Harris", "email": "thomas93@example.net", "job_title": "Architect",
     "company": "Hernandez-Lopez", "address": "2296 Johnson Stream\nWest Amy, AZ 15632", "last_login": "2024-04-10"},
    {"id": 20, "name": "Paul Rodriguez", "email": "wcoleman@example.net", "job_title": "Surveyor, rural practice",
     "company": "Russell and Sons", "address": "98144 Brown Island\nWest Nicolemouth, PA 24706",
     "last_login": "2023-08-11"},
    {"id": 21, "name": "Kimberly Miller", "email": "sarah04@example.org", "job_title": "Public relations officer",
     "company": "Brown-Johnson", "address": "71395 Steven Parks\nSouth Sarahport, SC 66532",
     "last_login": "2023-01-22"},
    {"id": 22, "name": "Jennifer Garcia", "email": "qpeterson@example.org", "job_title": "Scientist, water quality",
     "company": "Baker, Wilson and Lee", "address": "9360 Jason Ramp\nSouth Jessica, OK 20387",
     "last_login": "2023-04-09"},
    {"id": 23, "name": "Michael Davis", "email": "qwalker@example.net", "job_title": "Public relations officer",
     "company": "Jones-Thompson", "address": "708 Johnson Pass Suite 692\nMichaelmouth, TN 15848",
     "last_login": "2022-04-20"},
    {"id": 24, "name": "Eric Smith", "email": "sandra77@example.com", "job_title": "Editor, commissioning",
     "company": "Peterson-Hernandez", "address": "596 Johnson Creek Suite 086\nLake James, VT 04051",
     "last_login": "2024-08-01"},
    {"id": 25, "name": "Matthew Hernandez", "email": "cwilson@example.net", "job_title": "Production manager",
     "company": "Smith, Mcdonald and Hernandez", "address": "2525 Rachel Locks Apt. 182\nNorth Elizabeth, WY 51475",
     "last_login": "2023-08-17"},
    {"id": 26, "name": "Richard Garcia", "email": "jason10@example.com", "job_title": "Air cabin crew",
     "company": "Johnson, Rodriguez and Fisher", "address": "6964 Daniel Drive\nWest Brian, ID 42805",
     "last_login": "2024-05-24"},
    {"id": 27, "name": "Matthew Hernandez", "email": "jennifer11@example.net", "job_title": "Horticultural consultant",
     "company": "Sanchez, Rodriguez and Diaz", "address": "632 Mark Alley\nNorth Michaelhaven, VT 68133",
     "last_login": "2022-04-18"},
    {"id": 28, "name": "Jennifer Garcia", "email": "jessica82@example.org", "job_title": "Building surveyor",
     "company": "White, Ramirez and Jones", "address": "2138 Johnson Alley Suite 092\nNorth Scottmouth, OK 49673",
     "last_login": "2024-01-20"},
    {"id": 29, "name": "Paul Rodriguez", "email": "patrick96@example.net", "job_title": "Social researcher",
     "company": "Lee Group", "address": "644 Scott Pass\nNorth Scott, ID 44342", "last_login": "2021-08-07"},
    {"id": 30, "name": "Kimberly Miller", "email": "rebeccamartinez@example.com", "job_title": "Architect",
     "company": "Turner PLC", "address": "416 Mary Mission Apt. 949\nChristinamouth, TX 11444",
     "last_login": "2022-07-28"}
]

#Lists
#1. Extract Specific Data: From the provided dataset, write a Python script to create and print a new list containing only the name of the first 5 entries.
first_five_names = [employee['name'] for employee in employee_data[:5]]
print(first_five_names)

#2. Filter by Condition: Write a Python function that accepts the dataset and a job title string as input. The function should return a list of dictionaries where the job_title matches the given string.
def filter_by_job_title_lc(data, job_title):
    return [employee for employee in data if employee['job_title'] == job_title]

job_to_find = "Public relations officer"
filtered_employees = filter_by_job_title_lc(employee_data, job_to_find)

print(f"Employees with the job title '{job_to_find}':")
for employee in filtered_employees:
    print(employee)

job_to_find_2 = "Architect"
filtered_employees_2 = filter_by_job_title_lc(employee_data, job_to_find_2)

print(f"\nEmployees with the job title '{job_to_find_2}':")
for employee in filtered_employees_2:
    print(employee)

#3. Transform and Sort: Create a new list containing tuples of (name, company) for each entry in the dataset. Then, sort this new list alphabetically by the company name and print the result.
name_company_tuples = [(entry['name'], entry['company']) for entry in employee_data]
sorted_by_company = sorted(name_company_tuples, key=lambda x: x[1])

for item in sorted_by_company:
    print(item)

#4. Aggregation: Calculate and return the total number of unique job titles present in the dataset.

def count_unique_job_titles(dataset):
    job_titles = [entry['job_title'] for entry in dataset]
    unique_job_titles = set(job_titles)
    return len(unique_job_titles)

total_unique_job_titles = count_unique_job_titles(employee_data)
print(f"Total number of unique job titles: {total_unique_job_titles}")

#5. Performance with Nested Lists: Create a function that, given the dataset, efficiently counts the number of times a company has a new employee logging in after their previous login timestamp. The function should store the login history in a nested list structure for each company, demonstrating how nested lists impact performance for this type of repeated, cross-referencing operation.
from datetime import datetime

def count_new_logins_with_nested_lists(employee_data):

    company_login_history = []
    new_login_count = {}

    for employee in employee_data:
        company_name = employee['company']
        employee_name = employee['name']
        last_login_str = employee['last_login']
        current_login_date = datetime.strptime(last_login_str, '%Y-%m-%d')

        company_found = False
        for company_record in company_login_history:
            if company_record[0] == company_name:
                company_found = True
                login_history = company_record[1]

                found_match = False
                for login_entry in login_history:
                    if login_entry[0] == employee_name:
                        found_match = True
                        previous_login_date = login_entry[1]
                        if current_login_date > previous_login_date:
                            new_login_count[company_name] = new_login_count.get(company_name, 0) + 1
                            login_entry[1] = current_login_date
                        break

                if not found_match:
                    login_history.append([employee_name, current_login_date])
                break

        if not company_found:
            company_login_history.append([company_name, [[employee_name, current_login_date]]])

    return new_login_count


login_counts_nested = count_new_logins_with_nested_lists(employee_data)
print(login_counts_nested)

#Tuple
#1. Data Integrity: Given a single entry from the dataset as a dictionary, extract the id, name, and email and store them in a tuple named user_info.
first_employee = employee_data[0]
user_info = (first_employee['id'],first_employee['name'],first_employee['email'])
print(user_info)

#2. Iteration with Tuples: Create a list of tuples, where each tuple contains (id, last_login) for every entry in the dataset. Iterate through this new list and print each tuple.
id_last_login_list = [(employee['id'],employee['last_login']) for employee in employee_data]

print("List of (id, last_login) tuples:")
for user_tuple in id_last_login_list:
    print(user_tuple)

'''
#3. Efficiency and Immutability: Explain why using a tuple for (id, email) as a dictionary key is better than using a list for the same purpose, focusing on Python's mutability rules. Write a short script to demonstrate this.
first_employee = employee_data[0]
user_key_tuple = (first_employee["id"], first_employee["email"])

user_details_dict = {
    user_key_tuple: {
        "name": first_employee["name"],
        "job_title": first_employee["job_title"]
    }
}

print("tuple key (correct):")
print(user_details_dict)
print(f"Value retrieved using tuple key: {user_details_dict[user_key_tuple]}")
print("\n" + "=" * 50 + "\n")

user_key_list = [first_employee["id"], first_employee["email"]]

print("dictionary key (incorrect):")
try:
    invalid_dict = {
        user_key_list: {
            "name": first_employee["name"],
            "job_title": first_employee["job_title"]
        }
    }
    print(invalid_dict)

except TypeError as e:
    print(f"error: {e}")
    print("list cannot be a dictionary key.")
'''
#4. Nested Data Access: For a given entry in the dataset, extract the full address string. Split the address into individual components (e.g., street, city, state, zip) and store them in a nested tuple structure. Print the state from this structure.
employee_entry = employee_data[0]

full_address = employee_entry['address']

street, city_state_zip = full_address.split('\n')

city_and_state_zip = city_state_zip.split(', ')
city = city_and_state_zip[0]

state_zip = city_and_state_zip[1].split(' ')
state = state_zip[0]
zip_code = state_zip[1]

address_components = (
    street,
    (city, (state, zip_code))
)

extracted_state = address_components[1][1][0]

print(f"The address components are: {address_components}")
print(f"The state from the nested tuple is: {extracted_state}")

#5. Data Serialization: Write a function that takes the list of dictionaries and converts it into a list of tuples. Each tuple should represent one dictionary entry. Ensure the order of data within each tuple is consistent. Explain why this approach might be more memory efficient but less readable for a human inspecting the data.
def convert_to_list_of_tuples(data):
    if not data:
        return []

    keys = list(data[0].keys())

    return [tuple(entry[key] for key in keys) for entry in data]

list_of_tuples = convert_to_list_of_tuples(employee_data)

for item in list_of_tuples:
    print(item)

#Dictionary
#1. Access and Modify: Write a script that accesses the email of the entry with id: 15. Then, update the job_title of the entry with id: 20 to "Senior Surveyor" and print the modified entry.
email_id_15 = ""
for entry in employee_data:
    if entry["id"] == 15:
        email_id_15 = entry["email"]
        break

print(f"employee with id 15 is: {email_id_15}")

for entry in employee_data:
    if entry["id"] == 20:
        entry["job_title"] = "Senior Surveyor"
        print(f"\nemployee with id 20 is:")
        print(entry)
        break

#2. Check for Key: Write a function that takes an id and the dataset. It should return True if an entry with that id exists, otherwise return False.
def check_id_exists(employee_id, dataset):
    return any(entry['id'] == employee_id for entry in dataset)

test_id_exists = 15
test_id_does_not_exist = 69

print(f"Does an entry with ID {test_id_exists} exist? {check_id_exists(test_id_exists, employee_data)}")
print(f"Does an entry with ID {test_id_does_not_exist} exist? {check_id_exists(test_id_does_not_exist, employee_data)}")

#3. Dynamic Filtering: Write a function that takes the dataset and a dictionary of filters (e.g., {"company": "Turner PLC", "job_title": "Retail merchandiser"}). The function should return a list of all entries that match all filter criteria.
def filter_by_criteria(data, filters):
    if not filters:
        return data

    filtered_list = []
    for entry in data:
        if all(entry.get(key) == value for key, value in filters.items()):
            filtered_list.append(entry)
    return filtered_list


filters1 = {"company": "Turner PLC", "job_title": "Retail merchandiser"}
matching_employees1 = filter_by_criteria(employee_data, filters1)
print("Filter 1: company = 'Turner PLC', job_title = 'Retail merchandiser'")
for employee in matching_employees1:
    print(employee)
print("-" * 50)

filters2 = {"name": "Matthew Hernandez"}
matching_employees2 = filter_by_criteria(employee_data, filters2)
print("Filter 2: name = 'Matthew Hernandez'")
for employee in matching_employees2:
    print(employee)
print("-" * 50)

filters3 = {"id": 16}
matching_employees3 = filter_by_criteria(employee_data, filters3)
print("Filter 3: id = 16")
for employee in matching_employees3:
    print(employee)
print("-" * 50)

#4. Data Aggregation with Dictionaries: Create a function that processes the dataset and returns a new dictionary. The keys of the new dictionary should be company names, and the values should be a list of all employees (full dictionary entries) working at that company.
from collections import defaultdict

def group_by_company(data):
    grouped_employees = defaultdict(list)
    for entry in data:
        company_name = entry.get('company')
        if company_name:
            grouped_employees[company_name].append(entry)
    return dict(grouped_employees)

employees_by_company = group_by_company(employee_data)

import json
print(json.dumps(employees_by_company, indent=4))

#5. Hashing and Collision Simulation: Explain how Python's dictionary handles hash collisions. Write a function that simulates a worst-case hashing scenario by assigning the same calculated hash value to multiple entries in the dataset. Measure the performance difference in lookup time between a normal and the worst-case scenario.
import timeit

def normal_dict_lookup_performance():
    normal_dict = {entry['id']: entry for entry in employee_data}
    keys_to_lookup = [entry['id'] for entry in employee_data]

    start_time = timeit.default_timer()
    for key in keys_to_lookup:
        _ = normal_dict[key]
    end_time = timeit.default_timer()

    return (end_time - start_time) / len(keys_to_lookup)


class WorstCaseKey:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return f"WorstCaseKey({self.key})"


def worst_case_dict_lookup_performance():
    worst_case_dict = {WorstCaseKey(entry['id']): entry for entry in employee_data}
    keys_to_lookup = [WorstCaseKey(entry['id']) for entry in employee_data]

    start_time = timeit.default_timer()
    for key in keys_to_lookup:
        _ = worst_case_dict[key]
    end_time = timeit.default_timer()

    return (end_time - start_time) / len(keys_to_lookup)

normal_avg_time = normal_dict_lookup_performance()
worst_case_avg_time = worst_case_dict_lookup_performance()

print(f"Average lookup time for normal dictionary: {normal_avg_time:.10f} seconds")
print(f"Average lookup time for worst-case dictionary: {worst_case_avg_time:.10f} seconds")

if normal_avg_time > 0:
    performance_difference = worst_case_avg_time / normal_avg_time
    print(f"\nWorst-case lookup is approximately {performance_difference:.2f} times slower than normal lookup.")

#Class and Objects
#1. Basic Class Creation: Define a Python class named User that takes id, name, and email as attributes during initialization (__init__). Create an instance of this class using the data from the first entry of the dataset and print its attributes.
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

first_entry = employee_data[0]

user = User(first_entry['id'], first_entry['name'], first_entry['email'])

print("User instance attributes:")
print(f"ID: {user.id}")
print(f"Name: {user.name}")
print(f"Email: {user.email}")

#2. Method Implementation: Add a method to the User class named get_user_info that returns a formatted string with the user's name and company. Use this method on the object you created in the previous question.
class User:
    def __init__(self, id, name, email, company):
        self.id = id
        self.name = name
        self.email = email
        self.company = company

    def get_user_info(self):
        return f"{self.name} works for {self.company}."

first_entry = employee_data[0]
user = User(first_entry['id'], first_entry['name'], first_entry['email'], first_entry['company'])

user_info_string = user.get_user_info()
print(user_info_string)

#3. Data Encapsulation: Refine the User class to make the _id and _email attributes "protected" (using a single underscore). Add a public method get_id() and a setter method set_email(new_email) that includes a basic email format validation.
import re

class User:
    def __init__(self, id, name, email, company):
        self._id = id
        self.name = name
        self._email = email
        self.company = company

    def get_id(self):
        return self._id

    def set_email(self, new_email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, new_email):
            raise ValueError("Invalid email format.")

        self._email = new_email
        print(f"Email for user {self.name} updated to {self._email}.")

    def get_user_info(self):
        return f"{self.name} works for {self.company}."

first_entry = employee_data[0]
user_instance = User(first_entry['id'], first_entry['name'], first_entry['email'], first_entry['company'])

print("--- Initial User Info ---")
print(user_instance.get_user_info())
print(f"User ID (via public method): {user_instance.get_id()}")
print(f"Current Email (accessing protected attribute): {user_instance._email}")

print("\n--- Updating Email ---")
try:
    user_instance.set_email("amber.p@newcompany.com")
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Attempting Invalid Email Update ---")
try:
    user_instance.set_email("invalid-email-format")
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Final User Info ---")
print(f"Final Email (accessing protected attribute): {user_instance._email}")

#4. Class Inheritance: Create a parent class Employee with attributes name and job_title. Create a child class Admin that inherits from Employee and adds a new attribute privileges. Initialize an instance of Admin using data from the dataset.
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

class Admin(Employee):
    def __init__(self, name, job_title, privileges):
        super().__init__(name, job_title)
        self.privileges = privileges

    def display_admin_info(self):
        print(f"Name: {self.name}")
        print(f"Job Title: {self.job_title}")
        print(f"Privileges: {self.privileges}")


admin_entry = employee_data[0]
admin_instance = Admin(
    admin_entry['name'],
    admin_entry['job_title'],
    ["can_hire", "can_fire", "manage_payroll"]
)

admin_instance.display_admin_info()

#5.Advanced Object Design: Design a class Company that can manage User objects. The Company class should have a method to hire new employees (adding User objects) and a method to display a report of all employees, including their IDs, names, and job titles. Demonstrate how changes to a User object (e.g., updating an email) are reflected within the Company object, explaining how references to objects work in Python.
import pandas as pd

class User:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.email = data.get("email")
        self.job_title = data.get("job_title")
        self.company = data.get("company")
        self.address = data.get("address")
        self.last_login = data.get("last_login")

class Company:
    def __init__(self):
        self.employees = []

    def hire_employee(self, employee):
        if isinstance(employee, User):
            self.employees.append(employee)
        else:
            print("Invalid object type. Please provide a User object.")

    def display_employees(self):
        if not self.employees:
            print("No employees in the company.")
            return

        employee_list = [
            {"ID": emp.id, "Name": emp.name, "Job Title": emp.job_title, "Email": emp.email}
            for emp in self.employees
        ]
        df = pd.DataFrame(employee_list)
        print(df.to_string(index=False))

my_company = Company()
user_objects = [User(data) for data in employee_data]
for user in user_objects:
    my_company.hire_employee(user)

print("--- Initial Employee Report ---")
my_company.display_employees()

employee_to_update = my_company.employees[0]
new_email = "amber@example.com"
employee_to_update.email = new_email
print(f"\n--- Updating email for Employee ID {employee_to_update.id} ---")
print(f"Amber Peterson's new email is: {employee_to_update.email}")
print("\n--- Updated Employee Report ---")
my_company.display_employees()

