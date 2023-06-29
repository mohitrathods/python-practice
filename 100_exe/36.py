#
""""""
"""
USE GENERATOR TO CREATE EVEN NO.s
"""
def generate():
    for i in range(5):
        if i%2==0:
            yield i

li = []
for i in generate():
    li.append(i)
print(li)

# a = [2,321,422,2124,4,4,4]
# for i in a:
#     assert i%2==0

ip = input()
print(eval(ip))