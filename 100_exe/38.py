import zlib
s = b"dsggggggggga"
a = zlib.compress(s)
print(a)

from timeit import Timer
t = Timer("for i in range(10):1+1")
print(t.timeit())