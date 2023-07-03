import csv
import dict_data as d
dictionary = d.master_dict

li = []
new = {}
final_list = []
for each in dictionary.keys():
    li.append(each)
    new[each] = [i for i in dictionary[each].values()]
    for j in new[each][6].values():
        new[each].append(j)
    new[each].append(each)
    del new[each][6]
    print(new[each])
    my_list = [new[each][-1]] + new[each][1:-1] + [new[each][0]]
    print(my_list)
    final_list.append(my_list)

# tabs = ['INVOICE TO','CUSTOMER ID','SUPPLIER_REF_SKU','QTY','NAME','ADDRESS','ADDRESS 2','ZIPCODE','CITY','COUNTRY','REFERENCE']
tabs = ['NAME','ZIPCODE','CITY','ADDRESS','REFERENCE','ADDRESS2','COUNTRY','CUSTOMER_ID','INVOICETo','Supplier_REF_SKU']

with open("master_file.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerow(tabs)
    writer.writerows(final_list)
