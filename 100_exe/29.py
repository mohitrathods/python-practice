class Rectangle():
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return print(self.l * self.w)
o = Rectangle(2,3)
o.area()

"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
class Shape():
    #override this method with subclass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        self.l = l
    def area(self):
        return self.l*self.l
o = Square(5)
print(o.area())""""""
"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
li = [1,2,3,4,5,6,7,8,9,10]
x = map(lambda x:x**2,filter(lambda x:x%2==0,li))
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
""""""
"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
li = [1,2,3,4,5,6,7,8,9,10]
x = map(lambda x:x**2,filter(lambda x:x%2==0,li))
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
