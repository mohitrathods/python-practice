'''
import_sale_order_Final.csv
'''
'''
{
  'Prartnernumber'(Customernumber): {
    'Address': ,
    'Address2': ,
    'Zipcode': ,
    'City': ,
    'Country': ,
    'REFERENCE': ,
        'PurchaseList': {      
                         'INVOICETo': ,      
                         'Customer_id':,      
                         'Supplier_REF_SKU':
                         }
  }
'''

import csv
master_dict = {}
csv_file = open('import_sale_order_Final.csv')
read_file = csv.DictReader(csv_file,delimiter=',')
# for row in read_file:
#     print(row)
for row in read_file:
    master_dict.update({
                        row.get('NAME'): {
                                          'Address':row.get('ADDRESS') ,
                                          'Address2':row.get('ADDRESS 2') ,
                                          'Zipcode':row.get('ZIPCODE') ,
                                          'City':row.get('CITY') ,
                                          'Country':row.get('COUNTRY') ,
                                          'REFERENCE':row.get('REFERENCE') ,
                                          'PurchaseList': {
                                                           'INVOICETo':row.get('INVOICE TO') ,
                                                           'Customer_id':row.get('CUSTOMER ID'),
                                                           'Supplier_REF_SKU':row.get('SUPPLIER_REF_SKU')}
                                          }})
print(master_dict)

print('1.Get Purchase List by Partner Name')
print('2.Get Partner information by partner name')
print('3.To show prepared dictionary form CSV file')
print('Format of Partner Name: "New Partner (0000-9999)"')
choice = 0
choice =int(input('Your choice:'))
while choice >0:
    if choice == 1:
        partner_name = input('Partner Name:')
        print(master_dict.get(partner_name) and master_dict.get(partner_name).get('PurchaseList') or "Record not found")
    elif choice == 2:
        partner_name = input('Partner Name:')
        print(master_dict.get(partner_name) and  master_dict.get(partner_name).values() or "Record not found")
    elif choice == 3:
        for key,value in master_dict.items():
            print('Partner Name:',key)
            print(value.keys())
    choice = int(input('\nYour choice:'))
