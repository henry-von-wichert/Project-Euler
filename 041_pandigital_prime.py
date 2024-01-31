import math

primes = [2]
def testx(x):   #mutierend!
    prim = True

    for p in primes:
        if p > (x**0.5): 
            break
        if x%p == 0:
            prim = False
            break
    return prim

for i in range(3, 10):
    if testx(i) == True:
        primes.append(i)

#print(primes)

def pan_n(n):
    ziff = range(1, n+1)
    nums = []
    i = int(9.5*10**(n-1))
    while i < int(9.8*10**(n-1)):
        pan = True
        stri = str(i)
        for z in ziff:
            if i%3 != 0: # so bekommt man natürlich keine primzahlen!
                pan = False
            elif str(z) not in stri:
                pan = False
        if pan:
            nums.append(i)
        i+=1
    
    return nums

nums = pan_n(9)


for x in range(3, len(nums)):
    i = len(nums)-x
    prove = nums[i]
    prime = True
    for i in range(2,int(math.sqrt(prove))):
        if prime and prove % i == 0:
            prime = False
    if prime:
        print(prove)
        quit()
