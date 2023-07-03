import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("New Sheet")

# sheet.write(1,1,'Sample')
# workbook.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/empty/empty.xlsx")

for i in range(10):
    for j in range(10):
        sheet.write(i,j,'Sample')
        workbook.save("/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/empty/empty.xlsx")
