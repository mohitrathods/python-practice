import os
import xlsxwriter
import xlrd,xlwt
import openpyxl
from openpyxl import load_workbook

class Product:
    def __init__(self):
        pass

    #-------------------------------------------------------------------------------------
    #create xlsx database/file with fields
    def createXlDatabase(self):
        #fields only needed and call this fun only if xl file is not available at location
        path = '/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/'
        files = {
                'master_inventory.xlsx' : ['product_name','product_sku','quantity','date_of_purchase','purchase_price','total_amount','sales_price','vendor_name'],
                'purchase.xlsx' : ['product_name','product_sku','quantity','purchase_price','total_amount','total_tax'],
                'inventory_movement.xlsx' : ['product_name','date_of_changes','quantity_changes','vendor','purchase','sell'],
                'sales.xlsx' : ['product_name','product_sku','quantity','purchase_price','total_amount','total_tax']
        }
        for file_name,values in files.items():
            if os.path.exists(path+file_name):
                if os.path.isfile(path+file_name):
                    pass
            else:
                workbook = xlsxwriter.Workbook(path+file_name)
                workbook.close()

                for each_file,field_array in files.items():
                    wb = xlwt.Workbook()
                    sheet = wb.add_sheet("New Sheet")
                    c = 0
                    for i in field_array:
                        sheet.write(0,c,i)
                        wb.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/"+each_file)
                        c += 1

    #-------------------------------------------------------------------------------------




    #get product input from user
    sku = 0
    def getInput(self):
        self.createXlDatabase()
        product_name = str(input("Enter product name : "))
        self.sku += 1
        quantity = int(input("Enter quantity : "))
        vendor_name = str(input("Enter vendor name : "))
        date_of_purchase = str(input("Enter date of purchase : "))
        purchase_price = float(input("Enter purchase price : "))


product = Product()
#add product only one
ip = int(input("To add product info into master inventory press 1 : "))
if ip == 1:
    product.getInput()
else:
    print("press 1 to add product info")