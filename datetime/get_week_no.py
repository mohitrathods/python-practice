""""""
"""
Get Week number of year by both (Sunday as First Day of week & Monday as First Day of week).
get week no and name from selected year 
where sunday and monday are the first day of week
"""
# import datetime,time,pytz,calendar,date
from datetime import date,datetime,time
import calendar,pytz

now = date.today()
weekday_in_digit = now.strftime("%w")

d = date.today() #in loop print dates as mentioned below
x = calendar.day_name[d.weekday()] #d.week day is date.weekday
y = calendar.firstweekday()
z = calendar.weekday(2023,3,12)



raise SystemExit()
# if y == z
print(d,x,y,z)

count = 0
obj = calendar.Calendar()

for i in range(1,13):
    for each_date in obj.itermonthdates(2023,i):
        xi = calendar.day_name[each_date.weekday()] #name of the current date
        # split_list = each_date. and
        print(f"{xi} : {each_date}")
        count += 1