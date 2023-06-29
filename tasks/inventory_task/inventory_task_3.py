#FOUR-------------------------------------------------
""""""
"""
In given document check whether index is even / odd if index 
Even ⇒ qty * 100 and edit the warehouse as : ‘even_san francisco’ .
Odd => qty - 100 and edit  the warehouse as : ‘odd_san francisco’.
"""

#open a file
# open a file
file1 = open("Inventory Task.txt", "r")

# read the file
# read_content = file1.read()
# print(read_content)
# file1.close()

c=1
start_line = 38
filee = open('Inventory Task.txt', 'r')
line = filee.readlines()
for i in line:
    if c >= 38:
        print(i) # to store data in new file or it canbe done here

    c += 1

filee.close()
raise SystemExit('exit')

count = 1
for i in mylist1:
    if i.get('warehouse', False) and i.get('quantity',False):
        # print(count%2)
        if count%2 != 0:
            i['quantity'] -= 100
            i['warehouse'] = 'odd_'+i['warehouse']
        else:
            i['quantity'] *= 100
            i['warehouse'] = 'even_'+i['warehouse']
    # new.append(i)
    count += 1
print(mylist1)
#















# from inventory_task import warehouse_dict
#
# x = warehouse_dict['san francisco']
# l = len(x)
# print(range(l))
# # raise SystemExit("exit")
#
# for i in range(l):
#     if i%2 == 0:
#         x[i]['quantity'] += 100
#         x[i]['warehouse'] = 'odd_san francisco'
#     else:
#         x[i]['quantity'] -= 100
#         x[i]['warehouse'] = 'even_san francisco'
# print(x)