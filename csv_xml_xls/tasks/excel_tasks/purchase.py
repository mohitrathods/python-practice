import datetime , time
from Inventory.taxcalculation import TaxCalculation
class Purchase(TaxCalculation):
    purchase_data = {}
    def __init__(self):
        
        self.purchase_data ={}

        
    def purchases(self,purchase_date,purchase_quantity,customer_name,basic_price,total_price):
        
#         if not self.purchase_data:
#             self.purchase_data={1:{'purchase_date':purchase_date,  'purchase_qty':purchase_quantity, 'customer_name':customer_name, 'basic_price':basic_price, 'total_price':total_price, 'purchase_order_no':purchase_order_no}}
#         else:
        
        next_id = max(self.purchase_data.keys() and self.purchase_data.keys() or [0])+1
#         counter =1
#         next_invoice ='PO/'
        
        next_invoice = 'PO/{0:05}'.format(next_id)
        
        self.purchase_data.update({next_id:{'purcahse_date':purchase_date,  'purchase_qty':purchase_quantity, 'customer_name':customer_name, 'basic_price':basic_price, 'total_price':total_price, 'purchase_order_no':next_invoice}})
#         counter+=1


# purchase_obj = Purchase()
# choice = 0
# choice = int(input('Enter Choice:'))
# print()
# while choice >0:
#     if choice == 1:
#         purchase_date = time.strftime("%Y/%m/%d %X")
#         purchase_quantity = int(input('Quantity to purchase:'))
#         customer_name = input('Customer Name:')
#         basic_price = int(input('Basic Price:'))
#         total_price = purchase_obj.get_tax(basic_price)#data from taxcalculation class
# #         purchase_order_no = int(input('Order No.'))
#         purchase_obj.purchases(purchase_date,purchase_quantity,customer_name,basic_price,total_price)
#         print('purchase:',purchase_obj.purchase_data)
#     else:
#         break
#      
#     choice = int(input('Enter Choice:'))