import os
import xlsxwriter
import xlrd
import xlwt
import openpyxl
from openpyxl import load_workbook
from xlutils.copy import copy

class Product:
    # -------------------------------------------------------------------------------------
    # create xlsx database/file with fields
    def createXlDatabase(self):
        # fields only needed and call this fun only if xl file is not available at location
        path = '/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/'
        files = {
            'master_inventory.xlsx': ['product_name', 'product_sku', 'quantity', 'purchase_price', 'total_amount', 'vendor_name', 'sales_price'],
            'purchase.xlsx': ['product_name', 'product_sku', 'quantity', 'purchase_price', 'total_amount', 'total_tax'],
            'inventory_movement.xlsx': ['product_name', 'date_of_changes', 'quantity_changes', 'vendor', 'purchase', 'sell'],
            'sales.xlsx': ['product_name', 'product_sku', 'quantity', 'purchase_price', 'total_amount', 'total_tax']
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

    # -------------------------------------------------------------------------------------

    # get product input from user add this data to main inventory
    def getInput(self):
        self.createXlDatabase()
        product_name = str(input("Enter product name : "))
        quantity = int(input("Enter quantity : "))
        sku = str(input("Enter sku : "))
        vendor_name = str(input("Enter vendor name : "))
        purchase_price = float(input("Enter purchase price : "))
        total_amount = purchase_price*quantity
        sell_price = float(input("Enter selling price : "))
        arr = [product_name, sku, quantity, purchase_price, total_amount, vendor_name, sell_price]
        workbook = xlrd.open_workbook("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
        worksheet = workbook.sheet_by_index(0)
        nth_row = worksheet.nrows
        nth_col = worksheet.ncols

        copy_wb = copy(workbook)
        copy_sheet = copy_wb.get_sheet(0)

        #check each value of sku if matches with input update else add entry
        for i in range(nth_col):
            each_sku = worksheet.cell_value(i,1)
            if each_sku == sku:
                print("hello! u got it UPDATE data from here")

            else:
                c = 0
                for each in arr:
                    copy_sheet.write(nth_row,c,each)
                    copy_wb.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
                    c+=1

    # -------------------------------------------------------------------------------------




product = Product()
# add product only one
ip = int(input("To add products(new inventory) into master inventory press 1, press enter to break : "))
if ip == 1:
    product.getInput()
    # IF any matches increment data
    # get all ip
    # read data from old
    # match with inputs
