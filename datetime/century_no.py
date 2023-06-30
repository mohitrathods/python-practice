""""""
"""
Get Datetime with century number and without century number. ie. 2018 & 18.
"""
import datetime
y = int(input("year : "))
m = int(input("month : "))
d = int(input("day : "))
dt = datetime.date(y,m,d)

print("without century",dt.strftime("%y"))
print("with century",dt.strftime("%Y"))