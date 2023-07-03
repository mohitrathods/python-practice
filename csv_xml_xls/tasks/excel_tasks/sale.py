import datetime,time
from Inventory.taxcalculation import TaxCalculation
class Sale(TaxCalculation):
    sale_data = {}
    def __init__(self):
        
        self.sale_data ={}

        
    def sales(self,sale_type,selling_date,sale_quantity,customer_name,basic_price,total_price):
        
#         if not self.sale_data:
#             self.sale_data={{'selling_date':selling_date,  'selling_qty':sale_quantity, 'customer_name':customer_name, 'basic_price':basic_price, 'total_price':total_price, 'sale_order_no':sale_order_no}}
#         else:
        next_id = max(self.sale_data.keys() and self.sale_data.keys() or [0])+1
        next_invoice = 'SO/'+str(next_id).zfill(6)

        self.sale_data.update({next_id:{'type':sale_type,'selling_date':selling_date,  'selling_qty':sale_quantity, 'customer_name':customer_name, 'basic_price':basic_price, 'total_price':total_price, 'sale_order_no':next_invoice}})
        return
        


# sale_obj = Sale()
# choice = 0
# choice = int(input('Enter Choice:'))
# while choice >0:
#     if choice == 1:
#         selling_date = time.strftime("%Y/%m/%d %X")
#         sale_quantity = int(input('Quantity to sale:'))
#         customer_name = input('Customer Name:')
#         basic_price = int(input('Basic Price:'))
# #         total_price = int(input('Net Price:')) #data from taxcalculation class
#         total_price =sale_obj.get_tax(basic_price)
#         print(total_price)
# #         sale_order_no = input('Order No.')
#          
#         sale_obj.sales(selling_date,sale_quantity,customer_name,basic_price,total_price,)
#         for key, value in sale_obj.sale_data.it:
#             print(key,value)
# #         print('Sale:',sale_obj.sale_data)
#     else:
#         break
#      
#     choice = int(input('Enter Choice:'))