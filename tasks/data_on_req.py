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
dictionary = [{'id': 1, 'name': '1', 'quantity': 1.0}, {'id': 2, 'name': '2', 'quantity': 2.0}, {'id': 3, 'name': '3', 'quantity': 3.0}, {'id': 4, 'name': '4', 'quantity': 4.0}, {'id': 5, 'name': '5', 'quantity': 5.0}] # [{},{},{}]
dataset = [(0, 0, {'id': 1, 'name': '1', 'quantity': 1.0}), (0, 0, {'id': 2, 'name': '2', 'quantity': 2.0}), (0, 0, {'id': 3, 'name': '3', 'quantity': 3.0})] # (0,0,{}), (0,0,{}), (0,0,{})
# dictionary = [] # [{},{},{}]
# dataset = [] # (0,0,{}), (0,0,{}), (0,0,{})
# ----------------------------------- ----  common function
def break_loop(keyword):
    ip = str(input(f"press 9 to break and perform other operations press enter to continue {keyword} data\n"))
    try:
        if ip == '9':
            print("Master dataset : ", dataset)
            print("Dictionary : ", dictionary)
            return True
    except KeyboardInterrupt:
        pass

# ----------------------------------------- add data to both dataset
def zero(command):
    while True:
        print("Enter product_id, name and quantity : \n")
        id = int(input("Enter product id : "))
        name = str(input("\nEnter product name : "))
        quantity = float(input("\nEnter product quantity : "))
        ele = (command,0,{'id':id, 'name': name, 'quantity' : quantity})
        dataset.append(ele)
        dictionary.append(ele[2])
        print("data added\n")

        if break_loop('adding'):
            break
        # x = break_loop('adding')
        # if x:
        #     break

# ----------------------------------------- with update id add into both database
def one(command):
    while True:
        print("Enter product_id, name and quantity and update_id to update data : \n")
        update_id = int(input("Enter update id : "))
        # id = int(input("Enter new product id : "))
        name = str(input("\nEnter product name : "))
        quantity = float(input("\nEnter product quantity : "))
        for i in dictionary:
            if i['id'] == update_id:
                i['name'] = name
                i['quantity'] = quantity
                print("data updated")
                break
            else:
                pass

        if break_loop('update'):
            break

# ---------------------------------------- to remove data based on id from MASTER_DICT dataset
def two(command):
    while True:
        id = int(input("enter id to delete dictionary list of dictionary : "))
        ele = (command,id,False)
        dataset.append(ele)
        for i in dictionary:
            if i.get('id') == id:
                dictionary.remove(i)
            if not i.get('id'):
                print("ID not found\n")

        if break_loop('deleting'):
            break

# ---------------------------------------- to remove data based on id from MASTER_RECORD dataset
def three(command):
    while True:
        id = int(input("enter id to delete dataset from master list of dataset : "))
        ele = (command, id, False)
        dataset.append(ele)
        for i in dataset:
            x = i[2]['id']
            if x == id:
                dataset.remove(i)
                break
            else:
                print("id not found")
                break
        print(dataset)

        if break_loop('deleting'):
            break

# ------------------------------------ list of tuples by user
def four(command):
    while True:
        print("Enter no to add tuple in dataset : \n")
        ip = int(input("enter no : "))
        ele = (command, ip)
        dataset.append(ele)

        if break_loop('adding'):
            break


# --------------------------------------- to remove all vals from MASTER_DICT_DATASET
def five(command):
    if dataset:
        dataset.clear()
        print(f"dataset cleared : {dataset}")
    else:
        print(f"dataset is already empty\n Master dataset : {dataset}")

def six():
    print(dataset)
    print(dictionary)

def seven(command):
    while True:
        input_li = str(input("enter numbers seprated by comma : "))
        li = input_li.split(',')
        fl = []
        for l in li:
            fl.append(int(l))
        ele = (command,'_',fl)
        dataset.append(ele)

        for i in fl:
            for di in dictionary:
                if di['id'] == i:
                    dictionary.remove(di)
                    print("reached")
        print(dictionary)
        print(dataset)

        if break_loop('deleting'):
            break

while True:
    print("Master dataset : ", dataset)
    print("Dictionary : ", dictionary)
    n = int(input("Enter 0 to insert data into datasets\n "
                  "Enter 1 to add data into dataset with updated_id\n "
                  
                  "Enter 2 to delete specific dictionary from dictionary dataset\n "
                  "Enter 3 to delete specific dictionary from master records dataset\n "
                  "Enter 4 to add tuples items in dataset\n "
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