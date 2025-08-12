import xlsxwriter

warehouse_dict = {}

mylist1 = [{'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
           {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'san francisco'},
           {'product': 'e-com10', 'quantity': 22.0, 'warehouse': 'san francisco'},
           {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'san francisco'},
           {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'san francisco'},
           {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'san francisco'},
           {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0269', 'quantity': 10.0, 'warehouse': 'san francisco'},
           {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'san francisco'},
           {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'san francisco'},
           {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
           {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
           {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7888', 'quantity': 125.0, 'warehouse': 'san francisco'},
           {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'san francisco'},
           {'product': 'furn_0789', 'quantity': 60.0, 'warehouse': 'chicago'},
           {'product': 'furn_6666', 'quantity': 60.0, 'warehouse': 'chicago'},
           {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'chicago'},
           {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'},
           {'product': 'e-com18', 'quantity': 22.0, 'warehouse': 'chicago'},
           {'product': 'e-com11', 'quantity': 33.0, 'warehouse': 'chicago'},
           {'product': 'e-com12', 'quantity': 26.0, 'warehouse': 'chicago'},
           {'product': 'e-com13', 'quantity': 30.0, 'warehouse': 'chicago'},
           {'product': 'furn_0096', 'quantity': 45.0, 'warehouse': 'chicago'},
           {'product': 'furn_0097', 'quantity': 50.0, 'warehouse': 'chicago'},
           {'product': 'furn_0098', 'quantity': 55.0, 'warehouse': 'chicago'},
           {'product': 'desk0004', 'quantity': 60.0, 'warehouse': 'chicago'},
           {'product': 'furn_7800', 'quantity': 60.0, 'warehouse': 'chicago'},
           {'product': 'furn_0269', 'quantity': 18.0, 'warehouse': 'chicago'},
           {'product': 'furn_1118', 'quantity': 2.0, 'warehouse': 'chicago'},
           {'product': 'furn_8855', 'quantity': 80.0, 'warehouse': 'chicago'},
           {'product': 'e-com07', 'quantity': 200.0, 'warehouse': 'chicago'},
           {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'chicago'},
           {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'chicago'},
           {'product': 'furn_5555', 'quantity': 50.0, 'warehouse': 'chicago'},
           {'product': 'furn_7777', 'quantity': 35.0, 'warehouse': 'chicago'},
           {'product': 'furn_7888', 'quantity': 150.0, 'warehouse': 'chicago'},
           {'product': 'e-com11', 'quantity': 120.0, 'warehouse': 'chicago'},
           {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'chicago'},
           {'product': 'e-com18', 'quantity': 25.0, 'warehouse': 'chicago'},
           {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'chicago'},
           {'product': 'furn_8888', 'quantity': 50.0, 'warehouse': 'san francisco'},
           {'product': 'e-com10', 'quantity': 25.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7777', 'quantity': 45.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7888', 'quantity': 75.0, 'warehouse': 'san francisco'},
           {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
           {'product': 'furn_8888', 'quantity': 45.0, 'warehouse': 'san francisco'},
           {'product': 'e-com06', 'quantity': 75.0, 'warehouse': 'san francisco'},
           {'product': 'furn_8855', 'quantity': 15.0, 'warehouse': 'san francisco'},
           {'product': 'furn_6666', 'quantity': 10.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7777', 'quantity': 100.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 100.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7777', 'quantity': 80.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7800', 'quantity': 16.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7800', 'quantity': 32.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 50.0, 'warehouse': 'san francisco'},
           {'product': 'furn_6666', 'quantity': 20.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
           {'product': 'e-com07', 'quantity': 80.0, 'warehouse': 'san francisco'},
           {'product': 'desk0005', 'quantity': 65.0, 'warehouse': 'san francisco'},
           {'product': 'furn_7800', 'quantity': 8.0, 'warehouse': 'san francisco'},
           {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
           {'product': 'e-com11', 'quantity': 5.0, 'warehouse': 'san francisco'},
           {'product': 'furn_6666', 'quantity': 5.0, 'warehouse': 'san francisco'},
           {'product': 'e-com11', 'quantity': 10.0, 'warehouse': 'san francisco'},
           {'product': 'desk00070', 'quantity': 100.0, 'warehouse': 'rajkot'},
           {'product': 'desk0006', 'quantity': 70.0, 'warehouse': 'rajkot'}]

for item in mylist1:
    if "warehouse" in item and "product" in item and "quantity" in item:
        warehouse = item["warehouse"]
        product = item["product"]
        quantity = item["quantity"]

        product_info = {
            "product": product,
            "quantity": quantity
        }

        if warehouse not in warehouse_dict:
            warehouse_dict.update({warehouse: [product_info]})
        else:
            found = False
            for existing in warehouse_dict[warehouse]:
                if existing["product"] == product:
                    existing["quantity"] += quantity
                    found = True
                    break
            if not found:
                warehouse_dict[warehouse].append(product_info)

print(warehouse_dict)

workbook = xlsxwriter.Workbook("warehouse_data.xlsx")

bold_center = workbook.add_format({'bold': True, 'align': 'center'})
center = workbook.add_format({'align': 'center'})
red_fill = workbook.add_format({'bg_color': '#FF9999', 'align': 'center'})

for warehouse, products in warehouse_dict.items():

    products.sort(key=lambda x: x["product"])
    worksheet = workbook.add_worksheet(warehouse)

    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 20)

    worksheet.write("A1", "Product", bold_center)
    worksheet.write("B1", "Quantity", bold_center)

    row = 1
    for item in products:
        product = item["product"]
        quantity = item["quantity"]

        format_to_use = red_fill if quantity > 90 else center

        worksheet.write(row, 0, product, format_to_use)
        worksheet.write(row, 1, quantity, format_to_use)
        row += 1

workbook.close()
print("Excel file created successfully.")