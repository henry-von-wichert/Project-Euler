def prime_gen(nmax):
    l = [2]
    for n in range(3,nmax,2):
        mods = {n%p for p in l}
        if 0 not in mods: l.append(n)
    return l

def is_prime(n):
    if n<0:return False
    f = 2
    while f < n:
        while n%f == 0:
            return False
            n = n // f
        f += 1
    return True


abmax = 100
primes = prime_gen(abmax)

def nsqr_gen(a,b):
    s = []
    n = 0
    while is_prime(p:=n**2+a*n+b):
        n+=1
        s.append(p)
    return {p for p in s}



maxprimes = 0
maxa = 0
maxb = 0

for a in range(-abmax,abmax+1):
    for b in primes:
        if (m:=len(nsqr_gen(a,b)))>maxprimes:
            maxprimes = m
            maxa,maxb = a,b

print(maxa,maxb,maxprimes,maxa*maxb) # Kann irgendwie nicht über 40 zählen...
print(sorted(nsqr_gen(maxa,maxb)))