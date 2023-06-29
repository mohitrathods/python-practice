di = dict()
def d(n):
    for i in range(n):
        di[i] = i**2
d(6)
print(di)


di = []
def d(n):
    for i in range(n):
        di.append(i**2)
d(6)
print(di[:3])

