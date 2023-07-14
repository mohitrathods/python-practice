# # a = [1,24,34,5,3,2,253,523,5,43,0]
# # res = list(filter(lambda x : x%2 == 0,a))
# # print(type(res))
# # print(res)
#
# # Filter all people having age more than 18, using lambda and filter() function
#
# ages = [12,24,5,3,212,23,4,45,324,23]
# age_filter = filter(lambda age : age >= 18, ages)
# print(list(age_filter)) # filter gives result if there is condition
#
# age_map = list(map(lambda age : age >= 18, ages))
# print(age_map) # map will give boolean status but not actual values if condition
#
# age_map_vals = list(map(lambda age : age * 18, ages))
# print(age_map_vals) # here in map, condition is not given (means : multiplication will be performed with all elements)
#
# # MAP AND FILTER WITH LIST OF WORDS
# goats = ['EMINEM', '2upac', 'Dr.dre', 'snoop dog']
# animals_filter = list(filter(lambda x : x != '2upac', goats))
# print(animals_filter) # here condition > x != '2upac' is given
#
# uppercase_map = list(map(lambda x : x.upper(), goats))
# print(uppercase_map) # here condition is not given in map (means : x.upper() will applied to all elements)
#

# REDUCE FUNCTION IN PYTHON
