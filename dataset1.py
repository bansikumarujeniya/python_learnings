dataset1 = [{"id": 1, "date": "2022-08-01", "amount": 500, "customer_id": 1, "salesman_id": 1},
            {"id": 2, "date": "2022-01-02", "amount": 1800.5, "customer_id": 1, "salesman_id": 2},
            {"id": 3, "date": "2023-05-03", "amount": 2200.75, "customer_id": 1, "salesman_id": 3},
            {"id": 4, "date": "2023-07-25", "amount": 1450, "customer_id": 1, "salesman_id": 4},
            {"id": 5, "date": "2020-06-18", "amount": 1300, "customer_id": 1, "salesman_id": 5},
            {"id": 6, "date": "2021-10-20", "amount": 2000, "customer_id": 2, "salesman_id": 1},
            {"id": 7, "date": "2021-12-02", "amount": 2100, "customer_id": 3, "salesman_id": 2},
            {"id": 8, "date": "2025-07-03", "amount": 1600, "customer_id": 4, "salesman_id": 3},
            {"id": 9, "date": "2024-03-31", "amount": 11800, "customer_id": 5, "salesman_id": 4},
            {"id": 10, "date": "2025-01-05", "amount": 17500, "customer_id": 2, "salesman_id": 5},
            {"id": 11, "date": "2025-04-06", "amount": 1900, "customer_id": 3, "salesman_id": 2},
            {"id": 12, "date": "2025-07-15", "amount": 1950, "customer_id": 4, "salesman_id": 1},
            {"id": 13, "date": "2025-07-15", "amount": 2050, "customer_id": 5, "salesman_id": 2},
            {"id": 14, "date": "2025-03-19", "amount": 3150, "customer_id": 2, "salesman_id": 3},
            {"id": 15, "date": "2025-04-14", "amount": 1700, "customer_id": 3, "salesman_id": 4},
            {"id": 16, "date": "2025-02-08", "amount": 1600, "customer_id": 4, "salesman_id": 5},
            {"id": 17, "date": "2024-09-17", "amount": 23000, "customer_id": 5, "salesman_id": 4},
            {"id": 18, "date": "2024-07-13", "amount": 22400, "customer_id": 3, "salesman_id": 1},
            {"id": 19, "date": "2025-06-20", "amount": 400, "customer_id": 2, "salesman_id": 2},
            {"id": 20, "date": "2024-10-29", "amount": 14000, "customer_id": 5, "salesman_id": 3}]


#list
# 1 Extract order IDs: Write a Python function that takes a list of order records (where each record is a list) and returns a new list containing only the order id for every order.
'''
def extract_order_ids(orders):
    return [order['id'] for order in orders]
order_ids = extract_order_ids(dataset1)

print(order_ids)
'''

#2 Filter recent orders: Given a list of order records, create a new list that includes only the orders placed on or after a specific date.
'''
specific_date = '2024-10-29'

recent_orders = [order for order in dataset1 if order['date'] == specific_date]
print(recent_orders)

# filter-lambda method:-
recent_orders_filtered = list(filter(lambda order: order['date'] == specific_date, dataset1))
for order in recent_orders_filtered:
    print(order)
'''
#tuple
#1 Create a list of tuples: Use a list of tuples to represent the entire dataset. How would you access the amount for the third order in the dataset?
'''
third_order = dataset1[2]

amount_for_third_order = third_order['amount']
print(f"{amount_for_third_order}")
'''
#2 Compare sales with tuples: Given two order tuples, order1 and order2, write a conditional statement to check if order1 has a larger sales amount than order2.

'''
order1 = (1, '2022-08-01', 500, 1, 1)
order2 = (2, '2022-01-02', 1800.5, 1, 2)
if order1[2] > order2[2]:
    print("Order 1 has a larger sales amount.")
else:
    print("Order 1 does not have a larger sales amount.")
'''

# dictionary
#1  Restructure data for easy lookup: Convert the list of order records into a dictionary where the order_id is the key, and the value is another dictionary containing the other order details (date, amount, customer_id, salesman_id).
'''
restructured_data = {}

for record in dataset1:
    order_id = record['id']
    order_details = record.copy()
    del order_details['id']

    restructured_data[order_id] = order_details

print(restructured_data)
'''
#2  Calculate total sales per salesman: Use a dictionary to store the total sales amount for each salesman_id. Iterate through the orders dataset and populate this dictionary.

'''
sales_by_salesman = {}

for order in dataset1:
    salesman_id = order['salesman_id']
    amount = order['amount']

    if salesman_id in sales_by_salesman:
        sales_by_salesman[salesman_id] += amount
    else:
        sales_by_salesman[salesman_id] = amount

print(sales_by_salesman)
'''

#3  Update an order amount: Write a function that takes an order_id and a new amount and updates the corresponding record in the dictionary-based dataset.
'''
def update_order_amount(order_id, new_amount, dataset1):
    for record in dataset1:
        if record['id'] == order_id:
            record['amount'] = new_amount
            print(f"Order {order_id} updated. New amount: {new_amount}.")
            return
    print(f"Order {order_id} not found.")

update_order_amount(20, 15000, dataset1)
update_order_amount(8, 5000, dataset1)
update_order_amount(5,5000,dataset1)
'''
#4 Find orders for a specific customer: Given a customer_id, write a script that iterates through your dictionary-based dataset and returns a list of all orders placed by that customer.
'''
def find_orders_for_customer(dataset1,customer_id):
    customer_orders = []
    for order in dataset1:
        if order['customer_id'] == customer_id:
            customer_orders.append(order)
    return customer_orders


customer_id_to_find = 5
orders_for_customer = find_orders_for_customer(dataset1, customer_id_to_find)

print(f"Orders for customer with ID {customer_id_to_find}:")
for order in orders_for_customer:
    print(order)
'''

# class and objects
#1 Create the Order class: Define a Python class named Order that has an __init__ method. The __init__ method should accept and initialize instance attributes for id, date, amount, customer_id, and salesman_id.
'''
    class order:
        def __init__(self, id, date, amount, customer_id, salesman_id):
            self.id = id
            self.date = date
            self.amount = amount
            self.customer_id = customer_id
            self.salesman_id = salesman_id

        def __repr__(self):
            return f"Order(id={self.id}, date='{self.date}', amount={self.amount}, customer_id={self.customer_id}, salesman_id={self.salesman_id})"

    order1 = order(1, "2022-08-01", 500, 1, 1)
    print(order1)

    orders = [order(**data) for data in dataset1]
    print(orders[:3])

    orders = [order(**data) for data in dataset1]
    print(orders[:5])
'''
#2 Using the Sale class, create a list of Sale objects from the given dataset1.
'''
class Sale:
    def __init__(self, id, date, amount, customer_id, salesman_id):
        self.id = id
        self.date = date
        self.amount = amount
        self.customer_id = customer_id
        self.salesman_id = salesman_id

    def __repr__(self):
        return (f"Sale(id={self.id}, date='{self.date}', amount={self.amount}, "
                f"customer_id={self.customer_id}, salesman_id={self.salesman_id})")

sales = [Sale(**data) for data in dataset1]

for s in sales[:5]:
    print(s)
'''

#3 Write a function that takes the list of Sale objects and a customer_id as input, then returns all sales made by that specific customer.
'''
def get_customer_sales(sales_data, customer_id):
    customer_sales = [sale for sale in sales_data if sale['customer_id'] == customer_id]
    return customer_sales

customer_sales_1 = get_customer_sales(dataset1, 1)
print(f"Sales for customer_id 1:\n{customer_sales_1}")
'''
#4 Write a method within the Sale class, get_sales_info, that returns a formatted string containing the transaction ID and amount, like "Sale ID: 1, Amount: 500".
'''
class Sale:
    def __init__(self, id, date, amount, customer_id, salesman_id):
        self.id = id
        self.date = date
        self.amount = amount
        self.customer_id = customer_id
        self.salesman_id = salesman_id

    def get_sales_info(self):
        return f"Sale ID: {self.id}, Amount: {self.amount}"


sale_objects = [Sale(**data) for data in dataset1]

for sale in sale_objects:
    print(sale.get_sales_info())
'''

#5 Iterate through dataset1 and create an instance of the SalesRecord class for each dictionary. Store all the SalesRecord objects in a new list called sales_records.
'''
class SalesRecord:
    def __init__(self,id,date,amount,customer_id,salesman_id):
        self.id = id
        self.date = date
        self.amount = amount
        self.customer_id = customer_id
        self.salesman_id = salesman_id

    def __repr__(self):
        return f"SalesRecord(id={self.id}, date='{self.date}', amount={self.amount}, customer_id={self.customer_id}, salesman_id={self.salesman_id})"

sales_records = []
for record in dataset1:
    sales_records.append(SalesRecord(**record))

for i in range(2):
    print(sales_records[i])
'''

#6 Write a function that takes the sales_records list as an argument and returns the total amount of all sales combined.
'''
def calculate_total_sales(sales_records):
    total_amount = 0
    for record in sales_records:
        total_amount += record['amount']
    return total_amount

total_sales = calculate_total_sales(dataset1)
print(f"The total amount of all sales is: {total_sales}")
'''
#7 Write a function that takes the sales_records list as an argument and returns the SalesRecord object with the highest amount.
'''
def find_highest_sales_records(sales_records):
    if not sales_records:
        return None

    highest_record = max(sales_records,key=lambda record:record['amount'])
    return highest_record

highest_sale = find_highest_sales_records(dataset1)

if highest_sale:
    print("The Sales record with the highest amount is:")
    print(highest_sale)
else:
    print("the list of sales record is empty.")
'''

#8 Write a function that takes a customer_id and the sales_records list as arguments. It should return a new list containing all SalesRecord objects for that customer. For example, find all sales for customer_id = 5.
'''
def find_sales_by_customer(customer_id, sales_records):
    customer_sales = []
    for record in sales_records:
        if record['customer_id'] == customer_id:
            customer_sales.append(record)
    return customer_sales

customer_sales = find_sales_by_customer(5, dataset1)

for sale in customer_sales:
    print(sale)
'''

#9 Create a Salesman class with the following attributes:id,sales_records(a list of SalesRecord objects associated with this salesman)
'''
class SalesRecord:
    def __init__(self, id, date, amount, customer_id, salesman_id):
        self.id = id
        self.date = date
        self.amount = amount
        self.customer_id = customer_id
        self.salesman_id = salesman_id

    def __repr__(self):
        return (f"SalesRecord(id={self.id}, date='{self.date}', "
                f"amount={self.amount}, customer_id={self.customer_id})")


class Salesman:
    def __init__(self, id):
        self.id = id
        self.sales_records = []

    def add_sales_record(self, record):
        if isinstance(record, SalesRecord):
            self.sales_records.append(record)
        else:
            raise TypeError("Only SalesRecord objects can be added.")

    def __repr__(self):
        return f"Salesman(id={self.id}, records={len(self.sales_records)})"


def create_salesman_objects(dataset):
    salesmen_dict = {}
    for record_data in dataset:
        salesman_id = record_data['salesman_id']

        sales_record = SalesRecord(
            id=record_data['id'],
            date=record_data['date'],
            amount=record_data['amount'],
            customer_id=record_data['customer_id'],
            salesman_id=salesman_id
        )


        if salesman_id not in salesmen_dict:
            salesmen_dict[salesman_id] = Salesman(id=salesman_id)

        salesmen_dict[salesman_id].add_sales_record(sales_record)

    return salesmen_dict


if __name__ == '__main__':
    salesmen = create_salesman_objects(dataset1)

    for salesman_id, salesman in salesmen.items():
        print(salesman)
        for record in salesman.sales_records:
            print(f"  - {record}")
'''
#10 Add a method to the Salesman class called calculate_total_sales(). This method should calculate and return the sum of all amounts in the salesman's sales_records list. Then, iterate through the salesmen list and print the total sales for each salesman.
'''
class Salesman:
    def __init__(self, salesman_id):
        self.salesman_id = salesman_id
        self.sales_records = []

    def add_sale(self, sale):
        self.sales_records.append(sale)

    def calculate_total_sales(self):
        return sum(record['amount'] for record in self.sales_records)

def process_sales_data(data):
    salesmen_dict = {}
    for record in data:
        salesman_id = record['salesman_id']
        if salesman_id not in salesmen_dict:
            salesmen_dict[salesman_id] = Salesman(salesman_id)
        salesmen_dict[salesman_id].add_sale(record)
    return list(salesmen_dict.values())

salesmen = process_sales_data(dataset1)

print("Sales Report:")
for salesman in salesmen:
    total_sales = salesman.calculate_total_sales()
    print(f"Salesman ID: {salesman.salesman_id}, Total Sales: {total_sales}")
'''

#11 Using your salesmen list and the calculate_total_sales() method, find and print the Salesman object who has the highest total sales.

class Salesman:
    def __init__(self, id):
        self.id = id
        self.total_sales = 0.0

    def calculate_total_sales(self, dataset):
        self.total_sales = sum(
            sale['amount'] for sale in dataset if sale['salesman_id'] == self.id
        )
        return self.total_sales

    def __repr__(self):
        return f"Salesman(id={self.id}, total_sales={self.total_sales})"

if __name__ == "__main__":
    salesman_ids = set(sale['salesman_id'] for sale in dataset1)
    salesmen_list = [Salesman(id) for id in salesman_ids]

    for salesman in salesmen_list:
        salesman.calculate_total_sales(dataset1)

    highest_salesman = max(salesmen_list, key=lambda s: s.total_sales)

    print(f"The salesman with the highest total sales is: {highest_salesman}")
    print(f"Total sales amount: {highest_salesman.total_sales}")