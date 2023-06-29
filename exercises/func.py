#nested level : easy
def outer(a,b,c=10):
    def add(c,d):
        return c-d
    def multi():
        return a*b*c
    return add(a,b),multi()
print(outer(4,5))

import timeit
x = timeit.timeit(stmt='outer()')
print(x)

#arg only
def arg(*a):
    for i in a:
        print(i)
arg(34,3,5,34,534)

#keywords and arg
table = {'Person A':'Age A','Person B':'Age B','Person C':'Age C'}

def kw(kwargs):
    for i,j in kwargs.items():
        print(i,'is ',j)
kw(name="a",age=23)


def outer(x):
    def inner(y):
        return x+y
    return inner
a = outer(5) # returns inner fun as object | a = inner
res = a(3) # a(3) = inner(3)
print(res)

#decorator
