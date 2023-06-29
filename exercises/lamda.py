
new_d = {'product': 'furn_0789', 'quantity': 16.0, 'warehouse': 'san francisco'}
# print('a')
# print(type(new_d),"abc")
# print(new_d['warehouse'])
li = []
f = list( filter(lambda x : x != 'san francisco', new_d.values()))
print(f)