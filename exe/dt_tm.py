# Calculate number of days between two given dates
from datetime import timedelta, datetime
# # 2020-02-25
date_1 = datetime(2020, 2, 25)
#
# # 2020-09-17
date_2 = datetime(2020, 9, 17)
# Expected output:
#
# 205 days
print(date_2-date_1)

# ------------------------------------------
#
# Add a week (7 days) and 12 hours to a given date
# Given:
#
# # 2020-03-22 10:00:00--------------
# given_date = datetime(2020, 3, 22, 10, 0, 0)
# mins = 24*60*7+12*7
# addition = timedelta(minutes=mins)
# new = given_date+addition
# print(new)
# Expected output:
#
# 2020-03-29 22:00:00
# ------------------------------------------
#
# Print a date in a the following format
# Day_name  Day_number  Month_name  Year
# Refer: Python DateTime Format Using Strftime()
#
# Given:-----------
# givenn_date = datetime(2020, 2, 25)
# print(givenn_date.strftime("%d-%m-%Y"))
#
# Expected output:
# Tuesday 25 February 2020
# ------------------------------------------
# Convert string into a datetime object
# For example, You received the following date in string format. Please convert it into Python’s DateTime object.
#
# Refer: Python String to DateTime
#
# Given:
# date_string = "Feb 25 2020 04:20PM"
# x = datetime.strptime(date_string, "%b %d %Y %H:%M%p")
# print(x)
#
# Expected output:
# 2020-02-25 16:20:00
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
