import model_xlrd
location = ("/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/demo/file_example_XLS_100.xls")

#open the workbook
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

#for row and col 0,0
# print(sheet.cell_value(0,1))
#
# for i in range(101):
#     for j in range(101):
#         print(sheet.cell_value(i,j))

import pandas as pd

# Read the file
data = pd.read_csv("/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/demo/file_example_XLS_100.xls", low_memory=False)

# Output the number of rows
print("Total rows: {0}".format(len(data)))

# See which headers are available
print(list(data))