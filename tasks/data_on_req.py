""""""
# if num between 1 to 6 get user input
# get data on 0,1,4 th input else print coming soon...
# TAGS : name, product_id, quantity (price)
"""
T1 : if num = 0 > enter details in list until user wanna break
[]
item format = (input,0,{di of data}) // multiple items in list

T2 : if num = 1 > format is below
[]
item format = (input, update_id, {})

T3 : format []
item format = (input, user_input until break)

T4 : for no. 2 : DELETE ITEM FROM DATADICT
enter no 2 : delete record from master dataset which contains only dictionaries
take id if > delete from dataset of dict else
take all things as element add it into master record dataset

T5 for no. 3 : DELETE ITEM FROM DATASET

"""
master_db = [] # [{},{},{}]
master_dataset = [] # (0,0,{}), (0,0,{}), (0,0,{})

# ----------------------------------- ----  common function
# def break_loop(keyword):
#     ip = str(input(f"press 9 to break and perform other operations press enter to continue {keyword} data\n"))
#     try:
#         if ip == '9':
#             print("Master dataset : ", master_dataset)
#             print("Master DB : ", master_db)
#             break
#     except KeyboardInterrupt:
#         pass

# ----------------------------------------- add data to both dataset
def zero(command):
    while True:
        print("Enter product_id, name and quantity : \n")
        id = int(input("Enter product id : "))
        name = str(input("\nEnter product name : "))
        quantity = float(input("\nEnter product quantity : "))
        ele = (command,0,{'id':id, 'name': name, 'quantity' : quantity})
        master_dataset.append(ele)
        master_db.append(ele[2])

        ip = str(input("press 9 to break and perform other operations press enter to continue adding data\n"))
        try:
            if ip == '9':
                print("Master dataset : ",master_dataset)
                print("Master DB : ",master_db)
                break
        except KeyboardInterrupt:
            pass

# ----------------------------------------- with update id add into both database
def one(command):
    while True:
        print("Enter product_id, name and quantity with update_id : \n")
        update_id = int(input("Enter update id : "))
        id = int(input("Enter product id : "))
        name = str(input("\nEnter product name : "))
        quantity = float(input("\nEnter product quantity : "))
        ele = (command, update_id, {'id': id, 'name': name, 'quantity': quantity})
        master_dataset.append(ele)
        master_db.append(ele[2])

        ip = str(input("press 9 to break and perform other operations press enter to continue adding data\n"))
        try:
            if ip == '9':
                print("Master dataset : ", master_dataset)
                print("Master DB : ", master_db)
                break
        except KeyboardInterrupt:
            pass

# ------------------------------------ list of tuples by user
def four(command):
    while True:
        print("Enter no to add tuple in database and dataset : \n")
        ip = int(input("enter no : "))
        ele = (command, ip)
        master_db.append(ele)

        ip = str(input("press 9 to break and perform other operations press enter to continue adding data\n"))
        try:
            if ip == '9':
                print("Master dataset : ", master_dataset)
                print("Master DB : ", master_db)
                break
        except KeyboardInterrupt:
            pass

# ---------------------------------------- to remove data based on id from MASTER_DICT dataset
def two(command):
    while True:
        id = int(input("enter id to delete dictionary from master list of dictionary : "))
        ele = (command,id,False)
        master_dataset.append(ele)
        for i in master_db:
            if i.get('id') == id:
                master_db.remove(i)
            if not i.get('id'):
                print("ID not found\n")

        ip = str(input("press 9 to break and perform other operations press enter to continue deleting data\n"))
        try:
            if ip == '9':
                print("Master dataset : ", master_dataset)
                print("Master DB : ", master_db)
                break
        except KeyboardInterrupt:
            pass

# ---------------------------------------- to remove data based on id from MASTER_RECORD dataset
def three(command):
    while True:
        id = int(input("enter id to delete dataset from master list of dataset : "))
        ele = (command, id, False)
        master_dataset.append(ele)
        for i in master_db:
            if i.get('id') == id:
                del master_dataset[id]
            else:
                print("Id not found\n")

        ip = str(input("press 9 to break and perform other operations press enter to continue deleting data\n"))
        try:
            if ip == '9':
                print("Master dataset : ", master_dataset)
                print("Master DB : ", master_db)
                break
        except KeyboardInterrupt:
            pass

# --------------------------------------- to remove all vals from MASTER_DICT_DATASET
def five(command):
    if master_dataset:
        master_dataset.clear()
        print(f"dataset cleared : {master_dataset}")
    else:
        print(f"dataset is already empty\n Master dataset : {master_dataset}")

def six():
    print(master_dataset)
    print(master_db)

def seven(command):
    input_li = str(input("enter numbers seprated by comma : "))
    li = input_li.split(',')
    for i in li:
        master_dataset.remove(i)
    print(master_db)

while True:
    print("Master dataset : ", master_dataset)
    print("Master DB : ", master_db)
    n = int(input("Enter 0 to insert data into datasets\n "
                  "Enter 1 to add data into dataset with updated_id\n "
                  "Enter 2 to delete specific dictionary from master dictionary dataset\n "
                  "Enter 3 to delete specific dictionary from master records dataset\n "
                  "Enter 4 to add tuples in both datasets\n "
                  "Enter 5 to empty the master dataset list\n "
                  "Enter 6 to display datasets\n "
                  "Enter 7 give a list of IDs and remove other values then IDs from master database dictionary\n "
                  "Enter no : "))
    if n == 3:
        three(n)
    elif n == 5:
        five(n)
    elif n == 6:
        six()
    elif n == 2:
        two(n)
    elif n == 0:
        zero(n)
    elif n == 1:
        one(n)
    elif n == 4:
        four(n)
    elif n == 7:
        seven(n)

    breakloop = str(input("Enter 0 to break\n press enter to continue performing operaions : "))
    try:
        if breakloop == '0':
            break
    except KeyboardInterrupt:
        pass