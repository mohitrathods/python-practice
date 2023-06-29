
a = []
b = []
c = []
d = []
li = [a,b,c,d]

while True:
    ans = str(input("press 'y' to add value, press enter to break : "))
    if ans == 'y':
        ip = int(input("Enter no to add : "))
        for i in li:
            for i in range(len(li)-1):
                for j in range(len(li)-i-1):
                    if sum(li[j]) > sum(li[j+1]):
                        li[j],li[j+1] = li[j+1],li[j]
            li[0].append(ip)
            break
        print(a,b,c,d,end='  \n')
    else:
        break