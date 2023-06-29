""""""
"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
a = 5
b = 0
try:
    if a/b:
        print("try")
except:
    print("error")
finally:
    print("finally")

try:
    with open('28.py','r') as r:
        content = r.read()
    try:
        with open('29.py','a') as writelines:
            writelines.write(content)
    except:
        print("some error")
    finally:
        r.close()
except:
    print("error while opening file")
finally:
    print("task complete")
