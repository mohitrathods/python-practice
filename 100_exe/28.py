""""""
"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
li = [1,2,3,4,5,6,7,8,9,10]
x = filter(lambda x : x*x if x %2==0 else '' , li)
print(list(x))

"""
print even numbers with range
"""
l = list(filter(lambda f:f%2==0, range(1,100)))
print(l)

"""
Define a class named American which has a static method called printNationality.
"""
class American():
    @staticmethod
    def printNatinallu():
        print("called")
o = American()
o.printNatinallu()
American.printNatinallu()
