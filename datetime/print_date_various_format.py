""""""
"""
Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM
"""
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d"))
print(datetime.datetime.now().strftime("%d-%m-%Y"))
print(datetime.datetime.now().strftime("%m-%d-%Y"))
print(datetime.datetime.now().strftime("%d-%m-%Y"))
print(datetime.datetime.now().strftime("%Y-%d-%m"))