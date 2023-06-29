# a = [1,2,34,0]
# x = all(i >= 0 for i in a )
# print(x)
#all returns true if all items in the list matches condition

divisable = [2,5,7]
non_div = [10]

x = [print(i) for i in range(1,10000) if (all(i%j==0 for j in divisable) and all(i%k!=0 for k in non_div))]

# for i in range(1,100000):
#     if all(i%j == 0 for j in divisable):
#         if all(i%k != 0 for k in non_div):
#             print(i)