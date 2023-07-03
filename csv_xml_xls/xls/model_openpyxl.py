from model_openpyxl import Wo
# workbook = Workbook()
# spreadsheet = workbook.active
# spreadsheet["A1"] = "abc"
# spreadsheet["B1"] = "def"
# workbook.save(filename="/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/empty/empty.xlsx")

workbook = openpyxl.load_workbook('/home/setu/PycharmProjects/python-practice/csv_xml_xls/xls/demo/file_example_XLS_100.xls')
worksheet = workbook['First Name']
print(worksheet)