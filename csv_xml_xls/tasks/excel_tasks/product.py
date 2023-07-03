import datetime, time
import xlsxwriter
from Inventory.sale import Sale
from Inventory.purchase import Purchase
from Inventory.taxcalculation import TaxCalculation
class Product(Sale, Purchase):
    def __init__(self,product_name,product_type):
        """
        :func:It generates a dictionary for product class and initialize product
        :param:product_name (Type: string)
        :param:product_type (Type: string)
        """
        
        self.product_data = {'product_name':product_name,
                             'product_type':product_type,
                             'purchase_order_no':[],
                             'sale_order_no':[]
                             }
        
    def product(self,profit,loss,available_quantity,sale_order_no=None,purchase_order_no=None):
        '''
        :func: It will prepare/update product dictionary
        :param:profit(Type:integer)
        :param:loss(Type:integer)
        :param:available_quantity(Type:integer)
        :param:sale_order_no(Default Argument)
        :param:purchase_order_no(Default argument)
        :return:
        '''
        
        if purchase_order_no :           
            self.product_data.update({'available_quantity':available_quantity,                                
                                      'profit':0,
                                      'loss':0})   
            self.product_data['purchase_order_no'].append(purchase_order_no)
        elif sale_order_no:
           
            self.product_data.update({'available_quantity':available_quantity,
                                                                
                                      'profit':profit,
                                      'loss':loss})
            self.product_data['sale_order_no'].append(sale_order_no)      
        return
    
    def product_excel(self,product_worksheet):
        '''
        :func: Writes an excel file in Master_File.xlsx and sheet name:Purchase
        :param:purchase_worksheet (Type :  'xlsxwriter.worksheet.Worksheet' ,It is worksheet with name purchase_worksheet with sheet name:Purchase
        :return: It will return purchase_worksheet  to main and save in main workbook
        '''    
        row = 0
        col = 0
        for col_name,data in self.product_data.items():
            product_worksheet.write(row, col,col_name)
            col+=1
        row+=1
        col = 0
        for col_name, data in self.product_data.items():
            
            if col_name in ['purchase_order_no','sale_order_no']:
                product_worksheet.write(row,col,','.join(data))
            else:
                product_worksheet.write(row, col,data)
            col+=1
    
        return product_worksheet

    def purchase_excel(self,purchase_worksheet):
        '''
        :func: Writes an excel file in Master_File.xlsx and sheet name:Purchase
        :param:purchase_worksheet (Type :  'xlsxwriter.worksheet.Worksheet' ,It is worksheet with name purchase_worksheet with sheet name:Purchase
        :return: It will return purchase_worksheet  to main and save in main workbook
        '''    
        row = 0
        col = 0
        flag = False
        
        for col_name, data in Purchase.purchase_data.items():
            col = 0
            purchase_worksheet.write(row, col, col_name)
            if not flag:
                for row_name, row_data in data.items():
                    
                    purchase_worksheet.write(row, col, row_name)
                    col+=1
                    flag = True
                row+=1
                col = 0   
            for row_name, row_data in data.items():
                purchase_worksheet.write(row , col, row_data)
                col += 1
            row+=1
        return purchase_worksheet
      
    def sale_excel(self,sale_worksheet):
        '''
        :func: Writes an excel file in Master_File.xlsx and sheet name:Sale
        :param:sale_worksheet (Type:  'xlsxwriter.worksheet.Worksheet', it is worksheet with name sale_worksheet with sheet name:Sale)
        :return: It will return sale_worksheet  to main and save in main workbook
        '''    
        row = 0
        col = 0
        flag = False
        
        for col_name, data in Sale.sale_data.items():
            col = 0
            sale_worksheet.write(row, col, col_name)
            if not flag:
                for row_name, row_data in data.items():
                    sale_worksheet.write(row, col, row_name)
                    col+=1
                    flag = True
                row+=1
                col = 0   
            for row_name, row_data in data.items():
                sale_worksheet.write(row , col, row_data)
                col += 1
            row+=1
        return sale_worksheet



print("Initialize Product Information here!\n\nChoose Product type : stockable or consumable or service\n")
product_name = input("Product Name:")
product_type = input('Product Type:')

while product_type not in ['stockable' , 'consumable' , 'service']:
    print("You've entered wrong type of product!!!\nPlease enter a right product type")
    product_type = input('Product Type:')

product_obj = Product(product_name,product_type)
sale_order_no=""
purchase_order_no=""
profit=0
loss=0
available_quantity=0
for key, value in product_obj.product_data.items():
    print(key,":",value)
print("Press 1 for Purchase product")
print("Press 2 for Sale product")
print('Press 3 to Generate EXCEL file')
choice = 0
choice = int(input('Enter Choice:'))
while choice >0:
    if choice == 1:
        purchase_date = time.strftime("%Y/%m/%d %X")
        customer_name = input('Customer Name:')
        purchase_quantity = int(input('Quantity to purchase:'))
        pur_basic_price = float(input('Basic Price:'))
        print("Total Price",pur_basic_price*purchase_quantity)
        total_price = product_obj.get_tax(purchase_quantity*pur_basic_price)#data from taxcalculation class
        print("SGST: ",product_obj.calculate_sgst,"\nCGST: ",product_obj.cgst,"\nNet Price: ",total_price)
        product_obj.purchases(purchase_date,purchase_quantity,customer_name,pur_basic_price,total_price)
        available_quantity += purchase_quantity
        purchase_order =product_obj.purchase_data.get(max(product_obj.purchase_data.keys() and product_obj.purchase_data.keys() or [0]))
        purchase_order_no = purchase_order and purchase_order.get('purchase_order_no')
        product_obj.product( profit, loss,available_quantity,purchase_order_no=purchase_order_no)        
#         product_obj.purchase_data.
        for key, value in product_obj.purchase_data.items():
        
            s ="".join(str(i).ljust(30) for i in value.keys())
            print("ID".ljust(5),s)
            continue
        print("\n---------------------------------------------------------------------------------------------------------")
        for key, value in product_obj.purchase_data.items():
        
            s ="".join(str(i).ljust(30) for i in value.values())
            print(str(key).ljust(5),s)
        print("---------------------------------------------------------------------------------------------------------\n")
        
        print("\n====================================================")
        for key, value in product_obj.product_data.items():
            print(str(key).ljust(30),"|",str(value).ljust(30))
        print("====================================================\n")
            
    elif choice == 2:
        
        if Purchase.purchase_data:
            
            if product_type in ['stockable','consumable']:
                sale_type =product_type
                selling_date = time.strftime("%Y/%m/%d %X")                    
                customer_name = input('Customer Name:')
                sale_quantity = int(input('Quantity to sale:'))
                sale_basic_price = float(input('Basic Price:'))                    
                total_price =product_obj.get_tax(sale_quantity*sale_basic_price)
                available_quantity =purchase_quantity- sale_quantity
                product_obj.sales(sale_type,selling_date,sale_quantity,customer_name,sale_basic_price,total_price)
                    
                if pur_basic_price > sale_basic_price:
                    loss = sale_basic_price - pur_basic_price
                elif pur_basic_price < sale_basic_price:
                    profit = pur_basic_price - sale_basic_price

                sale_order =product_obj.sale_data.get(max(product_obj.sale_data.keys() and product_obj.sale_data.keys() or [0]))
                sale_order_no = sale_order and sale_order.get('sale_order_no')
                product_obj.product(abs(profit), abs(loss),available_quantity,sale_order_no=sale_order_no)                    
                for key, value in product_obj.sale_data.items():
                    s ="".join(str(i).ljust(30) for i in value.keys())
                    print("ID".ljust(5),s)
                    continue
                print("\n---------------------------------------------------------------------------------------------------------")
                for key, value in product_obj.sale_data.items():
                
                    s ="".join(str(i).ljust(30) for i in value.values())
                    print(str(key).ljust(5),s)
                print("---------------------------------------------------------------------------------------------------------\n")
                
                print("\n====================================================")
                for key, value in product_obj.product_data.items():
                    print(str(key).ljust(30),"|",str(value).ljust(30))
                print("====================================================\n")
            elif product_type in ['service']:
                sale_type = product_type
                selling_date = time.strftime("%Y/%m/%d %X")
                customer_name = input('Customer Name:')                                       
                sale_basic_price = float(input('Basic Price of service cost:'))
                total_price =product_obj.get_tax(sale_basic_price)
                
                product_obj.sales(sale_type,selling_date,customer_name,sale_basic_price,total_price,sale_order_no)
                    
                if pur_basic_price > sale_basic_price:
                    loss = sale_basic_price - pur_basic_price
                elif pur_basic_price < sale_basic_price:
                    profit = pur_basic_price - sale_basic_price
                    
                sale_order =product_obj.sale_data.get(max(product_obj.sale_data.keys() and product_obj.sale_data.keys() or [0]))
                sale_order_no = sale_order and sale_order.get('sale_order_no')
                product_obj.product(abs(profit), abs(loss),available_quantity,sale_order_no=sale_order_no)                    
                for key, value in product_obj.sale_data.items():
                
                    s ="".join(str(i).ljust(30) for i in value.keys())
                    print("ID".ljust(5),s)
                    continue
                print("\n---------------------------------------------------------------------------------------------------------")
                for key, value in product_obj.sale_data.items():
                
                    s ="".join(str(i).ljust(30) for i in value.values())
                    print(str(key).ljust(5),s)
                print("---------------------------------------------------------------------------------------------------------\n")
                
                print("\n====================================================")
                for key, value in product_obj.product_data.items():
                    print(str(key).ljust(30),"|",str(value).ljust(30))
                print("====================================================\n")
 
        else:
            print("Stock is empty, Please purchase!")
    elif choice == 3:
        workbook = xlsxwriter.Workbook('Master_file.xlsx')
        purchase_worksheet = workbook.add_worksheet('Purchase')
        sale_worksheet = workbook.add_worksheet('Sale')
        product_worksheet = workbook.add_worksheet('Product')
        product_obj.purchase_excel(purchase_worksheet)
        product_obj.sale_excel(sale_worksheet)
        product_obj.product_excel(product_worksheet)
        workbook.close()
    else:
        break
    choice = int(input('Enter Choice:'))

