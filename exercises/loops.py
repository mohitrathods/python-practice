#pascal triangle
#5-0,1,2,3,4
a,b = 0,1
for i in range(10):
    print(a)
    a,b = b,a+b

size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()