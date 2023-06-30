""""""
"""
CSV : comma seprated values
"""
import csv
with open("business_employment_data_small.csv",'r') as csv_reader:
    reader = csv.reader(csv_reader,delimiter='"')
    for line in reader:
        print(','.join(line))

with open("fill_files/empty.csv",'w',newline='') as file:
    writer = csv.writer(file)
    with open("business_employment_data_small.csv",'r') as write_lines:
        w = csv.reader(write_lines)
        for i in w:
            writer.writerow(i)

# field names
fields = ['Name', 'Email']

# data rows of csv file
rows = [['Nikhil', 'nikhil.gfg@gmail.com'],
        ['Sanchit', 'sanchit.gfg@gmail.com'],
        ['Aditya', 'aditya.gfg@gmail.com'],
        ['Sagar', 'sagar.gfg@gmail.com'],
        ['Prateek', 'prateek.gfg@gmail.com'],
        ['Sahil', 'sahil.gfg@gmail.com']]
with open("fill_files/empty (copy).csv",'w') as f:
    f = csv.writer(f)
    f.writerow(fields)
    f.writerows(rows)