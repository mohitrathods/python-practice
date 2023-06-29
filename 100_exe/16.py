""""""
"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

import time

time_nanosec = time.time_ns()
print(time_nanosec)

x = list(filter(lambda x:x%2!=0, range(10)))
print(x)

time_nano = time.time_ns()
print(time_nano)
print(time_nano-time_nanosec)

# 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