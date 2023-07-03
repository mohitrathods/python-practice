# import csv,task_csv_to_dict_to_csv
# with open("annual_enterprise_survey.csv",'r') as file:
#     dictreader_obj = csv.DictReader(file)
#     for i in dictreader_obj:
#         # print(i)
#         pass
#
# x = task_csv_to_dict_to_csv.new_list
# cols = [i for i in range(1,12+1)]
# with open("fill_files/empty (4th copy).csv", 'w') as f:
#     writer = csv.DictWriter(f,cols)
#     writer.writeheader()
#     fi = csv.writer(f)
#     fi.writerows(x)

for i in range(10):
    for lt in range(i,10):
        print("*",end="")
    for rt in range(i,10):
        print("*",end="")
    print('\n')
