import os
import xlsxwriter
import xlrd
import xlwt
import openpyxl
from xlutils.copy import copy

# open = xlrd.open_workbook("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
# sheet = open.sheet_by_index(0)
# sheet.get
"""
REF. : https://stackoverflow.com/questions/2725852/writing-to-existing-workbook-using-xlwt
"""

"""
READ EXCEL
"""
workbook = xlrd.open_workbook("/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
# worksheet = workbook.sheet_by_index(0) #get access 0,1 the sheet
# print(worksheet.cell_value(1,2)) #print specific value
#
# print(f"total rows filled : {worksheet.nrows}")
# print(f"total cols filled : {worksheet.ncols}")

# make writable copy of opened excel file
wb = copy(workbook)
ws = wb.get_sheet(0)
ws.write(2,1,'Modified!')
wb.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/inventory_task_main/data/master_inventory.xlsx")
