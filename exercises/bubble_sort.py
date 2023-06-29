arr = [53,12,5,654,7,95,64]
len = len(arr)

swap = False
for i in range(len-1):
    for j in range(len-i-1):
        if arr[j] > arr[j+1]:
            swap = True
            arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swap:
            break
print(arr)