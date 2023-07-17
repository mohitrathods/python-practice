# Return the string without its vowels ('y' is not a vowel in this case).
li = ['Abjure', 'Future', 'Picnic', 'Agonistic', 'Garland', 'Protect', 'Airline', 'Gigantic', 'Publish', 'Bandit', 'Goofy', 'Quadrangle', 'Banquet', 'Government', 'Recount', 'Binoculars', 'Grandnieces', 'Redoubtable', 'Biologist', 'Handbook', 'Reflection', 'Blackboard', 'Himself', 'Reporter', 'Board', 'Indulge', 'Ring', 'Bookworm', 'Inflatable', 'Salesclerk', 'Butterscotch', 'Inimical', 'Snapshot', 'Camera', 'Interim', 'Shellfish', 'Campus', 'Invest', 'Ship', 'Catfish', 'Jackpot', 'Significance', 'Carsick', 'Kitchenette', 'Sometimes', 'Celebrate', 'Law', 'Sublime', 'Celery', 'Life', 'Tabletop', 'Citizen', 'Lifeline', 'Teamwork', 'Coloring', 'Love', 'Tennis', 'Compact', 'Magnificent', 'Timesaving', 'Dark', 'Malevolence', 'Tree', 'Damage', 'Man', 'Termination', 'Dangerous', 'Mascot', 'Underestimate', 'Decorum', 'Marshmallow', 'Vineyard', 'Endorse', 'Mine', 'War', 'Engender', 'Moonwalk', 'Way', 'Erratic', 'Near', 'Wealth', 'Envelope', 'Nephogram', 'Wednesday', 'Etymology', 'Newborn', 'World', 'Eyewitness', 'Noisome', 'Xerox', 'Eulogy', 'Owl', 'You', 'Fish', 'Parenthesis', 'Zestful', 'Food', 'Perpetrator', '', 'Foreclose', 'Phone']
l = ['a','e','i','o','u']

final = list(map(lambda x : ''.join(list(map(lambda i : i if i not in l else '',x))), li))
print(final)
#---------------------------------------------------------

# Filter (keep) all the spells in spells with more than two 'a' characters.
li1 = ['Abjure', 'Future', 'Picnic', 'Agonistic', 'Garland', 'Protect', 'Airline', 'Gigantic', 'Publish', 'Bandit', 'Goofy', 'Quadrangle', 'Banquet', 'Government', 'Recount', 'Binoculars', 'Grandnieces', 'Redoubtable', 'Biologist', 'Handbook', 'Reflection', 'Blackboard', 'Himself', 'Reporter', 'Board', 'Indulge', 'Ring', 'Bookworm', 'Inflatable', 'Salesclerk', 'Butterscotch', 'Inimical', 'Snapshot', 'Camera', 'Interim', 'Shellfish', 'Campus', 'Invest', 'Ship', 'Catfish', 'Jackpot', 'Significance', 'Carsick', 'Kitchenette', 'Sometimes', 'Celebrate', 'Law', 'Sublime', 'Celery', 'Life', 'Tabletop', 'Citizen', 'Lifeline', 'Teamwork', 'Coloring', 'Love', 'Tennis', 'Compact', 'Magnificent', 'Timesaving', 'Dark', 'Malevolence', 'Tree', 'Damage', 'Man', 'Termination', 'Dangerous', 'Mascot', 'Underestimate', 'Decorum', 'Marshmallow', 'Vineyard', 'Endorse', 'Mine', 'War', 'Engender', 'Moonwalk', 'Way', 'Erratic', 'Near', 'Wealth', 'Envelope', 'Nephogram', 'Wednesday', 'Etymology', 'Newborn', 'World', 'Eyewitness', 'Noisome', 'Xerox', 'Eulogy', 'Owl', 'You', 'Fish', 'Parenthesis', 'Zestful', 'Food', 'Perpetrator', '', 'Foreclose', 'Phone']

# each = "asdfasdf"
# x = list(filter(lambda i : 'a' in i, each))
# print('a' in 'a')
# print(x)
mf = filter(lambda each : len(list(filter(lambda i : 'a' in i, each)))>=2,li1)
print(list(mf))

#-----------------------------------------------------------------------------------------------

# Make All the elements in upper case useing map()
# lst1=['Citizen', 'Lifeline', 'Teamwork', 'Coloring', 'Love', 'Tennis', 'Compact', 'Magnificent', 'Timesaving', 'Dark', 'Malevolence', 'Tree', 'Damage', 'Man', 'Termination', 'Dangerous', 'Mascot', 'Underestimate', 'Decorum', 'Marshmallow', 'Vineyard', 'Endorse', 'Mine', 'War',]
# m = list(map(lambda x : x.upper(),lst1))
# print(m)

# round all the numbers using map()
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# round = list(map(lambda x : round(x,2),circle_areas))
# print(round)

# filter out those who passed with scores more than 75...using filter()
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# find = filter(lambda l : l>75, scores)
# print(list(find))

# A palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same backwards as forwards. Let's filter out words that are palindromes from a tuple (iterable) of suspected palindromes.
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
# d = filter(lambda x : x[::-1] == x, dromes)
# print(list(d))

# Use map to print the square of each numbers rounded
# to three decimal places
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# m = list(map(lambda each : round(each*each,3),my_floats))
# print(m)

# Use filter to print only the names that are less than
# or equal to seven letters
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# f = list(filter(lambda x : len(x) >= 7,my_names))
# print(f)

# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# x = filter(lambda x : x , list1)
# print(list(x))

# Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])

# Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# l = lambda x,y : x+y
# m = map(lambda x,y : x+y, list1,list2)
# print(list(m))

# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# numbers = [1, 2, 3, 4, 5, 6, 7]
# m = list(map(lambda m: m*m,numbers))
# print(m)

# Given a two Python list. Write a program to iterate both lists simultaneously and display items
# from list1 in original order and items from list2 in reverse order.
# Given:
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# p = list(map(lambda x,y : str(x) + "   " + str(y),list1,list2[::-1]))
# print(p)

# Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# li = []
# fun = lambda i : li.append(i) if i not in li else ''
# for each in list1:
#     fun(each)
# print(li)





# Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
# Given:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# le1 = len(l1)
# le2 = len(l2)
# one = list(map(lambda x,index : x if index % 2 != 0 else '', l1,range(0,le1)))
# two = list(map(lambda x,index : x if index % 2 == 0 else '', l2,range(0,le2)))
# l = one+two
# l3 = [i for i in l if i != '']
# print(l3)





