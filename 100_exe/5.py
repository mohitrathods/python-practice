""""""
"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class A:
    def __init__(self):
        self.ip = ""
    def getstring(self):
        ip = input("enter string : ")
        self.ip = ip
    def printstring(self):
        print(self.ip)

o = A()
o.getstring()
o.printstring()