#find most 3 common chars from string
from collections import Counter
ip = "hehellosnonlksdfrdcccc"
x = Counter(ip)
sorted(x.values())print(sorted(x))