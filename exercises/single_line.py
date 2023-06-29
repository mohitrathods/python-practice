mylist1 = [
    {'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'},
    {'product': 'furn_6666', 'quantity': 16.0, 'warehouse': 'san francisco'},
    {'product': 'e-com08', 'quantity': 18.0, 'warehouse': 'san francisco'},
    {'product': 'e-com07', 'quantity': 500.0, 'warehouse': 'chicago'}
]

warehouse_dict = {}

for item in mylist1:
    warehouse = item['warehouse'] # = san francisco
    if warehouse in warehouse_dict: # if san francisco in empty dict
        warehouse_dict[warehouse].append(item) # emptydict['san francisco'].append(item = entire list)
    else:
        warehouse_dict[warehouse] = [item] # else : warehouse_dict['san francisco'] = [item = entire list]

for warehouse, items in warehouse_dict.items():
    print(warehouse)
    print(items)
    print()