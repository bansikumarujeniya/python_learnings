class CustomerMaster:
    auto_id = 1
    all_customers = []

    def __init__(self, name , pan_no , phone_no , customer_type):
        for customer in CustomerMaster.all_customers:
            if customer.pan_no == pan_no:
                raise ValueError("PAN number must be unique")

        while any(c.customer_id == CustomerMaster.auto_id for c in CustomerMaster.all_customers):
            CustomerMaster.auto_id += 1

        self.customer_id = CustomerMaster.auto_id
        self.name = name
        self.pan_no = pan_no
        self.phone_no = phone_no
        self.customer_type = customer_type

        CustomerMaster.auto_id += 1
        CustomerMaster.all_customers.append(self)

    def __str__(self):
        return f"{self.customer_id}: Customer_name: {self.name} | PAN No: {self.pan_no} | Phone No: {self.phone_no} | Customer_Type: {self.customer_type}"



class ProductMaster:
    auto_id = 1
    all_products = []

    def __init__(self, name , incoming , outgoing):
        for product in ProductMaster.all_products:
            if product.name.lower() == name.lower():
                raise ValueError("Product name must be unique")

        while any(p.product_id == ProductMaster.auto_id for p in ProductMaster.all_products):
            ProductMaster.auto_id += 1

        self.product_id = ProductMaster.auto_id
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
        self.on_hand_stock = incoming - outgoing

        ProductMaster.auto_id += 1
        ProductMaster.all_products.append(self)

    def update_stock(self,quantity,transaction_type):
        if transaction_type == "incoming":
            self.incoming  += quantity
        elif transaction_type == "outgoing":
            if quantity > self.on_hand_stock:
                raise  ValueError("Not enough stock")
            self.outgoing += quantity
        self.on_hand_stock = self.incoming - self.outgoing

    def __str__(self):
        return f"{self.product_id}: Product_name: {self.name} | Incoming: {self.incoming} | Outgoing: {self.outgoing} | On-Hand Stock: {self.on_hand_stock}"



class StockMaster:
    auto_id = 1
    all_transactions  = []

    def __init__(self, customer_name, product_name, quantity, transaction_type):
        customer = self.find_customer_by_name(customer_name)
        product = self.find_product_by_name(product_name)

        if not customer:
            raise ValueError("invalid customer name")
        if not product:
            raise ValueError("invalid product name")

        allowed = {
            "customer": ["outgoing"],
            "vendor": ["incoming"],
            "both": ["incoming", "outgoing"]
        }

        ctype = customer.customer_type.lower()
        if transaction_type not in allowed.get(ctype, []):
            raise ValueError(f"{ctype.title()} is not allowed to perform '{transaction_type}' transaction")

        while any(t.transaction_id == StockMaster.auto_id for t in StockMaster.all_transactions):
            StockMaster.auto_id += 1

        self.transaction_id = StockMaster.auto_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.transaction_type = transaction_type

        product.update_stock(quantity,transaction_type)

        StockMaster.auto_id += 1
        StockMaster.all_transactions.append(self)

    def find_customer_by_name(self,name):
        for cust in CustomerMaster.all_customers:
            if cust.name.lower() == name.lower():
                return cust
        return None

    def find_product_by_name(self,name):
        for prod in ProductMaster.all_products:
            if prod.name.lower() == name.lower():
                return prod
        return None

    def __str__(self):
        return f"Transaction {self.transaction_id}: Customer_Name: {self.customer_name} | Product_Name: {self.product_name} | Transaction_type: {self.transaction_type} | Quantity: {self.quantity}"

#############################################################################################################################################################################################
def main():
    while True:
        print("\n------------Stock Management--------------")
        print("1. Add Customer")
        print("2. Add Product ")
        print("3. Add Transaction")
        print("4. Show All Customers")
        print("5. Show All Products")
        print("6. Show All Transactions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        try:
            if choice == "1":
                name = input("Enter customer name: ")
                pan = input("Enter PAN number: ")
                phone = input("Enter phone number: ")
                ctype = input("Enter customer type (Customer/Vendor/Both): ")
                CustomerMaster(name,pan,phone,ctype)
                print("Customer added successfully")

            elif choice == "2":
                name = input("Enter Product name: ")
                incoming = int(input("Enter Incoming Stock: "))
                outgoing = int(input("Enter Outgoing Stock: "))
                ProductMaster(name, incoming, outgoing)
                print("Product added successfully")

            elif choice == "3":
                cname = input("Enter customer name: ")
                pname = input("Enter product name: ")
                qty = int(input("Enter quantity: "))
                ttype = input("Enter transaction type (incoming/outgoing): ").lower()
                if ttype not in ["incoming", "outgoing"]:
                    raise ValueError("Transaction type must be 'incoming' or 'outgoing'")
                StockMaster(cname, pname, qty, ttype)
                print("Transaction added successfully")

            elif choice == "4":
                print("\nAll Customers:")
                for c in CustomerMaster.all_customers:
                    print(c)

            elif choice == "5":
                print("\nAll Products:")
                for p in ProductMaster.all_products:
                    print(p)

            elif choice == "6":
                print("\nAll Transactions:")
                for t in StockMaster.all_transactions:
                    print(t)

            elif choice == "7":
                print("Exit")
                break

            else:
                 print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError as ve:
            print("❗ Error:", ve)
        except Exception as e:
            print("Something went wrong:", e)

if __name__ == "__main__":
    main()




fdh fgdfgbksbgbjbgibdfigbisdfgigb


 dfg hfdddddddgbsdg

