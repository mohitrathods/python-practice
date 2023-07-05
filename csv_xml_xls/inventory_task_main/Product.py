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
            'inventory_movement.xlsx': ['product_name', 'date_of_changes', 'quantity_changes', 'price', 'customer_name', 'vendor','purchase_or_cell'],
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
        li=[]

        workbook = xlrd.open_workbook("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
        worksheet = workbook.sheet_by_index(0)
        nth_row = worksheet.nrows
        nth_col = worksheet.ncols

        copy_wb = copy(workbook)
        copy_sheet = copy_wb.get_sheet(0)

        sku = str(input("Enter sku : "))

        flag = False
        j = 0
        x = None
        for i in range(nth_row):
            eachrow = worksheet.row(i)
            if eachrow[1].value == sku:
                flag = True
                j = i
                x = eachrow
                break

        if flag:
            print("UPDATE data here")
            add_qty = float(input(f"You have {x[2].value} quantity in stock > Add more stock > add quantity : "))
            total_qty = x[2].value + add_qty
            final_total = total_qty * x[3].value
            copy_sheet.write(j, 2, total_qty) # row,col,value
            copy_sheet.write(j, 4, final_total) # row,col,value
            copy_wb.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
            lastrow = worksheet.row(nth_row-1)
            for l in lastrow:
                # print(l.value,type(l.value))
                li.append(l.value)

        if not flag:
            print("ADD NEW DATA")
            product_name = str(input("Enter product name : "))
            quantity = int(input("Enter quantity : "))
            vendor_name = str(input("Enter vendor name : "))
            purchase_price = float(input("Enter purchase price : "))
            total_amount = purchase_price * quantity
            sell_price = float(input("Enter selling price : "))
            arr = [product_name, sku, quantity, purchase_price, total_amount, vendor_name, sell_price]
            c = 0
            for each in arr:
                copy_sheet.write(nth_row,c,each)
                li.append(each)
                c+=1
            copy_wb.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
        op = li.copy()
        li.clear()
        return op

    # -------------------------------------------------------------------------------------
