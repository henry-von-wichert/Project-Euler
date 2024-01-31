from math import log10, ceil

def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    else:
        for i in range (n-1):
            old, new = new, (old + new)
        return new

def length(n):
    leng = ceil(log10(n))
    return leng

n = 0
while True:
    n += 1
    leng = length(fibi(n))
    if leng == 1000:
        print(n)
        break