import time
from datetime import datetime
import pytz
import calendar

print(calendar.month(2023,4))

t = time.localtime()
print(t)

d = datetime.now()
print(d.strftime("%m-%b"))
#strftime = string format of time
