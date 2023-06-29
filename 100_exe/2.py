""""""
"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def fact(a):
    if a==0:
        return 1
    else:
        return a * fact(a-1)
print(fact(5))

facto =1 
for i in range(1,9):
    facto = facto*i

print(facto)