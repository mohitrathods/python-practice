""""""
"""
Diffrence of 2 Date times.
"""
from datetime import datetime,timedelta
import math


# datetime(year, month, day, hour, minute, second)
a = datetime(2017,3,23,16,35,36)
b = datetime(2023,6,22,17,30,56)
print(b-a)


"""
Addition of 2 date times
> Add time to a datetime object
"""
initialize = datetime(2023,5,1,11,11,11)
print("Original time : ",initialize)

#change or addition of minutes and seconds to current time > IT CHANGES DATES ALSO AS PER ADDITION OF entity
addition = timedelta(minutes=5252)
new_date_time = initialize + addition
print(new_date_time)



"""
Multiplication of time with integer and float
"""
# ip = float("enter hours : ") #if ip = 4.30 then time should be 4.30 >
ip = float(input("enter hours in float : "))

#round input to  1 decimal
r = round(ip,1) #round to 1 decimal point
xi = math.floor(ip) #floor

#convert hours into minutes
round_ti = round(xi-r,1) #round 0.543523

if round_ti < 0:
    round_ti = round_ti*-1

#convert rount_ti to min
minutes_after_point = round_ti*60


#pass minutes in timedelta function if ip = 4.9 > 4 hours + 0.9 hours

cur_time = timedelta(hours=xi,minutes=minutes_after_point)
print(cur_time)
