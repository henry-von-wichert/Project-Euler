import math

s = 0
#n = 7

#print(n) 

def collatz(n):
    s = 0
    while n > 1:
        if n/2 > int(n/2):
            n = 3*n+1
            s += 1
            #print(n) 
        else:
            n = n/2
            s += 1
            #print(n) 
    return s
#print("---")

x = 1
lengths = []

while x < 1000000:
    lengthspez = collatz(x)
    lengths.append(lengthspez)
    x +=1

maxl = max(lengths)
num = lengths.index(maxl) + 1

print(maxl,num)

#print(collatz(4))