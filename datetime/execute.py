import time
from datetime import date,datetime

current = datetime.now()
print("all : ",current)

year = current.year
print("year : ",year)

month = current.month
print("month : ",month)

day = current.day
print("current : ",day)

hour = current.hour
print("hour : ",hour)

minutes = current.minute
print("minutes : ",minutes)

seconds = current.second
print("seconds : ",seconds)

microsec = current.microsecond
print("microseconds : ",microsec)

#YEAR MONTH DAY FORMAT
ymd = datetime(2012,12,31)
print(ymd)

print(current.second*hour*minutes)
print(36111/365)

t1 = date(year=2023, month=12, day=18)
t2 = current.date()
print(t1-t2)

from datetime import timedelta
tx = timedelta(weeks=3,days=43,hours=435,seconds=2355532)
ty = timedelta(days=32,hours=545,minutes=4554,seconds=454345)
#weeks days hours mins secs


print(tx-ty)


d = datetime.now()
print(d.strftime("%d/%m/%Y"))
print(d.strftime("%H:%M:%S"))

#
#
#
# Get Current month name from date.
#
# Difference of 2 date time.quotient and the remainder. (divmod(t1, t2)). and get output of it in Various units. like hours, minutes, Days, months, seconds.
#
# Get Week number of year by both (Sunday as First Day of week & Monday as First Day of week).
#
# Get Day of year from date time. (01,...366).
#
# Get Locale’s equivalent of either AM or PM. from Date.
#
# Get Datetime with century number and without century number. ie. 2018 & 18.
#
# Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM
#

