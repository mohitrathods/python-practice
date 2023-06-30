""""""
"""
Get local timezone and current  UTC time. and Convert it in local timezone. also convert it in other timezone.
"""
from datetime import datetime
import time
import pytz

#locality
local = pytz.timezone("Asia/Kolkata")
#local date and time
t = time.localtime() #gives all the data get it in particular format below var = current_time
d = datetime.now() #gives all the data get it in particular format

current_time = time.strftime("%H:%M:%S", t)
current_date = d.strftime("%Y-%m-%d")
naive = datetime.strptime(f"{current_date} {current_time}", "%Y-%m-%d %H:%M:%S")
print(naive)

# local = Asia/Kolkata > localize time with asia/kolkata <:> it returns timing that asia/kolkata is 5:30 ahead of utc
local_dt = local.localize(naive,is_dst=None)
print("to local : ",local_dt)

# THIS PRINTS CURRENT TIME OF UTC BASED ON GIVEN INPUT TIME WHICH IS LOCALIZED
utc_dt = local_dt.astimezone(pytz.utc)
print("CURRENT UTC TIME based on given time localized as Asia/Kolkata : ",utc_dt)


print("Current UTC timezones BASED ON given time and LOCALIZED as EACH locality")
for locality in pytz.all_timezones:
    l = pytz.timezone(locality)
    answer = l.localize(naive,is_dst=None)
    utcdt = answer.astimezone(pytz.utc)
    print(f"CURRENT UTC TIME and DATES based on given time localized as {locality} : ",utcdt)
    # time.sleep(0.002)