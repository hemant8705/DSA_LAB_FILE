# Experiment 07: Inventory Stock Management System

inventory = []

def insert_product():
    sku = input("Enter SKU: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    inventory.append({"sku": sku, "name": name, "quantity": qty})
    print("Product Added!")
