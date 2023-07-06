import os
import xlsxwriter
import xlrd
import xlwt
import openpyxl
from openpyxl import load_workbook
from xlutils.copy import copy

path = '/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/testing/'
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
        worksheet = workbook.add_worksheet("Sheet1")
        c = 0
        for each in values:
            worksheet.write(0,c,each)
            c+=1
        workbook.close()