""""""
"""
Write a program to compute 1/2 + 2/3 + 3/4 + ...+n/n+1 with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
"""
sum = 0
float(sum)
for i in range(1,6):
    sum += float(i)/float(i+1)
print(round(sum,3))