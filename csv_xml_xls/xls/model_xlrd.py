import xlrd

#open the file using open_wb function
workbook = xlrd.open_workbook('/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/demo/file_example_XLS_100.xls')

#get list of sheet names using sheet_names method
# sheet_names = workbook.sheet_names()
# print("Sheet Names : ",sheet_names)

#access first sheet by index or name
# by_index = workbook.sheet_by_index(0)
# by_name = workbook.sheet_by_name('Sheet1')  # Access sheet by name

# print(by_name,by_index)

#extract data by cell_value method
# cell_value = by_index.cell_value(0, 0)
# print(cell_value)

#close workbook after read data
# workbook.close()

#----------------------

sheet_names = workbook.sheet_names()
print("Sheet Names : ",sheet_names)

#access the first sheet
sheet = workbook.sheet_by_index(0)

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        cell_value = sheet.cell_value(i,j)
        print(f"Cell ({i} {j}) : {cell_value}")
workbook.close()
