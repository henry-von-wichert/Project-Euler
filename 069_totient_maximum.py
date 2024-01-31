# das Maximum ist die Zahl mit den meisten verschiedenen Primfaktoren
from itertools import accumulate
primes = []

def testx(x):
    prim = True
    for p in primes:
        if p > (x**0.5): 
            break
        if x%p == 0:
            prim = False
            break
    return prim

for i in range(2, 50):
    if testx(i) == True:
        primes.append(i)
    
primes[0] = (2,1-1/2)

for t in accumulate(primes, func = lambda alt, neu: (alt[0]*neu, alt[1]*(1-1/neu))):
    n,p = t
    print(n, p)
