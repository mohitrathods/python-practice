""""""
"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
s = "Hello world!"
dic = {'upper' : sum(1 for i in s if i.isupper()), 'lower' : sum(1 for i in s if i.islower())}
print(dic)

