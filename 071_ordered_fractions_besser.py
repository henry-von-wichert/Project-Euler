dmax = 1000000
n0 = 3
d0 = 7
best = (0,1)
def fg(a,x): # a/b > x/y -> ay>bx 
    a,b = a # auspacken der Tupel
    x,y = x
    return a*y>b*x

for d in range(1,dmax+1):
    if fg(new :=((n0*d)//d0,d),best) and fg((n0,d0),new): best = new

print(best)