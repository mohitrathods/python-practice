import os
import xlsxwriter
import xlrd
import xlwt
import openpyxl
from openpyxl import load_workbook
from xlutils.copy import copy

workbook = xlrd.open_workbook('/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/empty_files/demo_file.xlsx')
worksheet = workbook.sheet_by_index(0)
nth_row = worksheet.nrows
nth_col = worksheet.ncols

print(worksheet.cell_value(0,1))
c = 0
for i in range(0,nth_row-1):
    print(worksheet.cell_value(c,i))
    c+=1