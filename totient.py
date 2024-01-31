import matplotlib.pyplot as plt
def hcf(a,b):
    if a < b: a,b = b,a # a > b OBdA
    while b:
        a,b = b, a%b
    return a

def phi1(n):
    if n==1: return 0
    p = 0
    for i in range(1,n):
        if hcf(n,i)==1:
            p+=1
    return p

print(phi1(9))
l = [n/phi1(n) for n in range(2,1000)]
plt.scatter(range(2,1000),l,s = 0.6)
plt.show()