def hcf(a,b):
    if a < b: a,b = b,a # a > b OBdA
    while b:
        a,b = b, a%b
    return a

def fg(a,x): # a/b > x/y -> ay>bx 
    a,b = a # auspacken der Tupel
    x,y = x
    return a*y>b*x

class Bruch():
    def __init__(self,n,d):
        self.n = n
        self.d = d
    def __gt__(self,other):
        return self.n * other.d > other.n * self.d
    def __lt__(self,other):
        return self.n * other.d > other.n * self.d
    def __str__(self):
        return f"{self.n}/{self.d}"
    def __eq__(self,other):
        return self.n * other.d == other.n * self.d

dmax = 1000
brueche = []
for d in range(1,dmax+1):
    for n in range(1,d):
        if hcf(d,n) == 1:
            brueche.append(Bruch(n,d))

brueche = sorted(brueche, reverse = True)

print(str(brueche[brueche.index(Bruch(3,7))-1]))