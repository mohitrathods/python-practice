# This time swap the map() and filter() functions so that map() function is inside filter() function.
# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive
# to the new list.
# lst4=[-1000, 500, -600, 700, 5000, -90000, -17500]
# mf = list(filter(lambda x : x < 0, lst4))
# new = list(map(lambda x : abs(x),mf))
# print(new)
#-------------------------------------------------------------------------------------------------------------------

# Using filter() function filter the list so that only negative numbers are left.
# lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
# f = filter(lambda x : x<0,lst1)
# print(list(f))

# Using filter function, filter the even numbers so that only odd numbers are passed to the new list.
# lst2=[22, 100, 19, 13, 11, 1, 4, 66]
# f1 = filter(lambda y: y%2 != 0, lst2)
# print(list(f1))

# Using filter() and list() functions and .lower() method filter all the vowels in a given string.
# str1="Winter Olympics in 2022 will take place in Beijing China"
# f2 = list(filter(lambda s : s.islower(), str1))
# print(f2)

# Using map() and filter() functions add 2000 to the values below 8000.
# lst3=[1000, 500, 600, 700, 5000, 90000, 17500]
# m1 = map(lambda x : x + 1000 if x < 8000 else x, lst3)
# print(list(m1))


# Write a program in Python to filter the given list if the given expression evaluates to true.
# li = [0, 3, 2, 30, 20, 34, 89, 35, 72, 64]
# # expr = (x % 4 == 0)
# tr = filter(lambda x : x % 4 == 0, li)
# print(list(tr))

# Exclude all the numbers from nums divisible by 3 or 5.
# numbers_range = 1, 100
# nums = filter(lambda x : x % 3 == 0 and x % 5 == 0 ,range(1,101))
# print(list(nums))

