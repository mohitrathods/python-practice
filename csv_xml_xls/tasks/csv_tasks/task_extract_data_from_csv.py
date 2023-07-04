import dict_data as d

data = d.master_dict

print("List of tasks")
print('1.Get Purchase List by Partner Name')
print('2.Get Partner information by partner name')
print('3.To show prepared dictionary form CSV file')
print('4.Format of Partner Name: "New Partner (0000-9999)"')
choice = 0
choice = int(input("enter choice : "))
while choice > 0:
    if choice == 1:
        partnername = str(input("enter partner name : "))
        print(data.get(partnername).get('PurchaseList') and data.get(partnername).values() or "data not found")
        break
    elif choice == 2:
        s = str(input("enter partner name for partner info : "))
        print(data.get(s).values() and data.get(s).items() or "data not found")
        break
    elif choice == 3:
        print("print prepared dict from csv file : ")
        for key,value in data.items():
            print(f"each item : {key} : {value}")
        break
    elif choice == 4:
        print(sorted(data.keys()))
        break