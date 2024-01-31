from math import isqrt

ps = [(n*(3*n-1))//2 for n in range(1,10001)]

Ds = []

def ispent(p):
    disk = 1+24*p
    sqrt = isqrt(disk)
    if sqrt*sqrt == disk:
        if sqrt%6 == 5:
            return True
    return False


for i,p in enumerate(ps):
    for o in ps[:i]:
        D = p-o
        S = p+o
        if ispent(D) and ispent(S):
            Ds.append((D,S,p,o))

Ds = sorted(Ds,key = lambda t: t[0])
print(Ds)

