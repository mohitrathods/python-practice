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
#

#
#
#
#
#
#
#
#
#
#
#

