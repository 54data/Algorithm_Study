n = int(input())
nlist = [0] * (21)
nlist[0] = 0
nlist[1] = 1

for i in range(2, len(nlist)):
    nlist[i] = nlist[i-1] + nlist[i-2]
    
print(nlist[n])