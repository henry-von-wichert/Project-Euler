with open("./Project Euler/pathsum2.txt","r") as file:
    tri = file.readlines()
    tri = [l.replace("\n","") for l in tri]
    tri = [[int(s) for s in l.split()] for l in tri]

while len(tri)>1:
    tri[-2] = [ sec + max(tri[-1][i],tri[-1][i+1]) for i,sec in enumerate(tri[-2])]
    tri.pop(-1)

print(tri)