""""""
"""
Write a program to compute:
f(n)=f(n-1)+100 when n>0 and f(0)=1
with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
500
"""

def fn(n):
    if n == 0:
        return 0
    if n > 0:
        x = (n-1)*100 + 100
        print(x)
fn(4)

#RECURSION 

def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))