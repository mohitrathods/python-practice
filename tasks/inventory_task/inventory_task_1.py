#TWO -----------------
"""
Take  warehouse , product , qty from user.
Check whether warehouse already exists in data then add product , and qty to related list of dictionary
else
Add all details into main dictionary(data) .
"""
from inventory_task import warehouse_dict

warehouse = str(input("enter warehouse name : "))

if warehouse in warehouse_dict:
    print(f"{warehouse} warehouse exists : add following data")
    product = str(input("enter product name : "))
    quantity = float(input("enter quantity : "))
    warehouse_dict[warehouse].append({'product':product,'quantity':quantity})
else:
    print(f"{warehouse} doesn't exists : add following data")
    warehouse = str(input("enter NEW warehouse name : "))
    product = str(input("enter product name : "))
    quantity = float(input("enter quantity : "))
    warehouse_dict[warehouse] = []
    warehouse_dict[warehouse].append({'product':product,'quantity':quantity})
    print("data added successfully")
print(warehouse_dict)