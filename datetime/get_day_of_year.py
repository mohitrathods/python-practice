""""""
"""
Get Day of year from date time. (01,...366).
get date and show no of date
"""
import datetime
import calendar

y = int(input("year : "))
m = int(input("month : "))
d = int(input("day : "))
# dt = datetime.date(year=y,month=m,day=d)

custom_Date = datetime.datetime(y,m,d)
day_of_year = custom_Date.strftime("%j")
day = custom_Date.strftime("%A")

print(day_of_year,day)