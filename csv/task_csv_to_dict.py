""""""
import csv
"""
convert csv to dict where > { keys : [values of column]
convert dict to original csv
"""

d = {}
l = []
with open("business_employment_data_small.csv",'r') as file:
    reader = csv.reader(file)
    for i in reader:
        l.append(i)

c = 0
# for each in l:
#     for j in range(12):
        # l[j] = d[c]
        # d[c] = each[j]
    # c += 1
for i in l[0]:
    d[i] = []
print(d)

values = []
lii = []
for m in range(0,12):
    for n in l:
        # print(n[m])
        lii.append(n[m])
    # print(lii)
    values.append(lii)
  # lii.clear()
print(values)

# for x in range(1,8):
#     #l[x] : x of list will value
#     for j in d:
#         d[j] = [i for i in l[j]]

# print(d)
#
# raise SystemExit()
#
# for x in d.keys():
#     d[x].append('abfa')
#
# print(d)