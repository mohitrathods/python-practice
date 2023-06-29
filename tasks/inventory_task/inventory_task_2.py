#THREE-------------------------------------------------
""""""
"""
Take  warehouse , product , qty from user , Check whether warehouse already exists in data and then add prod , and qty to related list of dictionary , 
> if product is already exists in data then calc quantity
> else add all details into main dictionary (data)
"""


warehouse_dict = {}

while True:
    ip = str(input("Enter 'y' to add more items (CONTINUE)\nPress ENTER to CLOSE : "))
    if ip in ['y','Y']:
        warehouse = str(input("enter warehouse name : "))

        if warehouse in warehouse_dict:
            print(f"{warehouse} warehouse exists : add following data to create new")
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
    else:
        print(warehouse_dict)
        break