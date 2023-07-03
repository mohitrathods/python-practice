""""""
import csv
"""
convert csv to dict where > { keys : [values of column] }
convert dict to original csv
"""

d = {}
l = []
with open("business_employment_data_small.csv", 'r') as file:
    reader = csv.reader(file)
    for i in reader:
        l.append(i)

"""
CSV TO DICTIONRAY
"""
for i in l[0]:
    d[i] = []
    l.remove(l[0])

c = 0
for key in d.keys():
   d[key] = [i[c] for i in l]
   c += 1

"""
dict to orignal csv write to new csv file
"""
#MERGE KEY AND VALUES IN ONE LIST
new_d = d.copy()
new_list = []

tabs = [k for k in d.keys()]
# print(tabs)
values = [v for v in d.values()]
# print(values)

for i in range(len(values[0])):
    row = []
    for each in values:
        row.append(each[i])
    new_list.append(row)
print(new_list)

with open("fill_files/empty (another copy).csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(tabs)
    writer.writerows(new_list)


#-----------------------------------------------------------------------------------------------------------------------
# values = [v for v in new_d.values()]
# print(values)
# # for i in range(161):
#
#
#     # for i in range(161):
#     #     x = []
#     #     for j in range(12):
#     #         ele = values[x]
#     #         x.append(ele)
#     #     print(x)
#     #     x.append(new_list)
# # print(len(new_list))
# raise SystemExit()
#
# co = 0
# # for i in range(161):
#     # x = [each[c] for each in values] #each[1] list =  x
#     # new_list.append(x) # append x to new
# x = []
# for each in values:
#     x.append(each[c])
#     co += 1
#     # new_list.append(x)
# print(new_list)
#
#

#
#
# #
# # raise SystemExit()
# #
# # counter = 0
# # for m in range(12):
# #     for i in l:
# #         pass
# #         # (d[keys[m]]) = [].append(i[counter])
# #
# #         # print(i[counter])
# #     counter += 1
# # # print(d)
# #
# # raise SystemExit("exit")
# # # print(type(d.keys()))
# # keys = list(d.keys())
# #
# # # for i in keys:
# # #     print(type(i))
# # # raise SystemExit()
# #
# # for m in range(0,12):
# #     for i in keys:
# #         d[i] = [k[m] for k in l]
# #
# #     # keys = list(d.keys())
# #
# # print(d)
# # # print([k[0] for k in l])
# # # print(l)
# # raise SystemExit()
# #
# # for j in range(0,12):
# #     for i in range(0, 161):
# #         li = [k[j] for k in l]
# #         d[str(keys[j])] = li
# #
# # print(d)
# # #
# # # values = []
# # # lii = []
# # # for m in range(0,12):
# # #     for n in d.values():
# # #         # print(n[m])
# # #         lii.append(n[m])
# # #     # print(lii)
# # #     values.append(lii)
# # #   # lii.clear()
# # # print(values)
# # #
# # # # for x in range(1,8):
# # # #     #l[x] : x of list will value
# # # #     for j in d:
# # # #         d[j] = [i for i in l[j]]
# # #
# # # # print(d)
# # # #
# # # # raise SystemExit()
# # # #
# # # # for x in d.keys():
# # # #     d[x].append('abfa')
# # # #
# # # # print(d)