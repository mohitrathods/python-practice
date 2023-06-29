""""""
"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
x = int(input("enter range : "))
li = []
for i in range(x):
    ip = str(input("enter sentence : "))
    li.append(ip.upper())

for i in li:
    print(i)