
# new_d = {'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'}
# print('a')
# print(type(new_d),"abc")
# print(new_d['warehouse'])
# li = []
# f = list( filter(lambda x : x != 'san francisco', new_d.values()))
# print(f)

# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
# sotred = lambda x : (sorted(i) for i in x)
# print(sorted(List))

# get second largest number from each list
# Get the second largest element
# secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
# res = secondLargest(List, sotred)
#
# print(res)

# Filter out all odd numbers using filter() and lambda function
# li = [5, 7, 22, 97,54, 62, 77, 23, 73, 61]
# l = lambda x : [i*2 for i in x]
# print(l(li))

# make strin in upper case with lambda
# str_ip = str(input("Enter string : "))
# ip_two = str(input("Enter two string : "))
# st = lambda a,b : a.upper() and b.lower()
# print(st(str_ip,ip_two))

#if string > firstcapitle | if float > round 3 | if - > absolute & float round 2| if int > i**2
a = ["hand",12.34,342.43242133241,1.00000000000000001, 'leg','tounge',-234,-324.5334,-4343.00000001,1,2,4,3425,5,53]
# f = map(lambda each : each.capitalize() if type(each) == str else each**2 if type(each) == int else round(each,3) if type(each) == float else abs(each) if each < 0 and type(each) == float else print(''),a)
f = map(lambda x : x.capitalize() if type(x) == str else abs(x) if type(x) == int and x < 0 else x*x if type(x) == int else round(x,3) if x >= 0 else round(abs(x),2) if type(x) == float and x < 0 else print(" "),a)
# print(list(f))
# ['Hand', 12.34, 342.432, 1.0, 'Leg', 'Tounge', 54756, 324.53, 4343.0, 1, 4, 16, 11730625, 25, 2809]

listttt = [1,2,3,-4,6-1,-89,53,6,6,6,6,4,98,9,7,63,-5,5-5,-5,-5-579,-2632]
# remove all duplicate and new li should have negative
# new_li = []
# filt = filter(lambda ele : new_li.append(ele) if ele not in new_li and ele < 0 else print(" "), listttt)

# use set to remove duplicate automatic
unique_list = list(set(listttt))
print(unique_list)

n = filter(lambda ele : ele < 0,listttt)

# n = filter(lambda ele : ele if ele < 0 else listttt.remove(ele) if ele in listttt else print(" "),listttt)
print(list(n)) 