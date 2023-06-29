#ONE ----------------
#Read above file and Separate list of dictionary according to the warehouse

import inventory_data
li = inventory_data.mylist1

warehouse_dict = {}
# raise SystemExit("exit")

for item in li:
    warehouse = item['warehouse'] # = san francisco
    if warehouse in warehouse_dict: # if san francisco in empty dict
        warehouse_dict[warehouse].append(item) # emptydict['san francisco'].append(item = entire list)
        del item['warehouse']
    else:
        warehouse_dict[warehouse] = [item] # else : warehouse_dict['san francisco'] = [item = entire list]

print(warehouse_dict)
"""
FINAL DICTIONARY ABOVE
"""