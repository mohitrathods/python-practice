# Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary
# to show the count of each element.
# Given:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# from collections import Counter
# d = Counter(sample_list)
# x = dict(d)
# print(x)

#---------------------------------------------------------------------------------

# Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
# # Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sample_dict["location"] = sample_dict["city"] # dictionary's new key = dict's old key's value
# # delete old key
# del sample_dict['city']
# print(sample_dict)
#-----------------------------------------------------------------------------------------------


# Generate 6 digit random secure OTP every single time
# for i in range(1,7):
#     print(random.randint(0,9),end='')

# Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
# SYMBOLS = ['@', '#', '$','?']
#
# l = []
# for i in range(1,7):
#     passw = 'n'
#     x = random.choice(DIGITS+UPCASE_CHARACTERS+LOCASE_CHARACTERS+SYMBOLS)
#     l.append(x)
#
# len = len(l)
# rand_pos = random.randint(0,len-1)
# # MUST : 2 upper case, 1 lower case, 1 special, 1 digit
# for i in range(1,3):
#     rand_position = random.randint(0, len - 1)
#     x = random.choice(UPCASE_CHARACTERS)
#     l.insert(rand_position,x)
# lc = random.choice(LOCASE_CHARACTERS)
# l.insert(rand_pos,lc)
# di = random.choice(DIGITS)
# l.insert(rand_pos,di)
# print(''.join(l))



# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# y = [random.choice(LOCASE_CHARACTERS) for j in range(1,4)]
# x = [random.choice(UPCASE_CHARACTERS) for i in range(1,3)]
# print(''.join(x+y))


# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)



# Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
# Given:
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)


# Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1: str1 = "JhonDipPeta"
# Output: Dip
# Case 2: str2 = "JaSonAy"
# Output: Son
# str1 = "JhonDipPeta"
# str2 = "JaSonAy"
# mid1 = len(str1)
# mid2 = len(str2)
# x = int(mid1/2)
# y = int(mid2/2)
# print(str1[x-1]+str1[x]+str1[x+1])
# print(str2[y-1]+str2[y]+str2[y+1])


# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Given:
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:
# AuKellylt
# mid = len(s1)
# x = int(mid/2)
# print(s1[:x]+s2+s1[x:])


# Count all letters, digits, and special symbols from a given string
# Given:
# str1 = "P@#yn26at^&i5ve"
# chars = 0
# digs = 0
# syms = 0
# for i in str1:
#     if i.isdigit():
#         digs+=1
#     elif i.isalpha():
#         chars+=1
#     else:
#         syms+=1
# print(f'total > digits : {digs}, chars = {chars}, syms : {syms}')


