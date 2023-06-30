""""""
"""
Get Locale’s equivalent of either AM or PM. from Date.
"""
import datetime,time
t = time.localtime()
curr = time.strftime("%H",t)
print(type(curr))
i = int(curr)
if i > 12 and i <= 24:
    print("PM")
else:
    print("AM")