nlist = [int(input()) for i in range(9)]

X = sum(nlist) - 100

for i in range(len(nlist)):
    for x in range(i+1, len(nlist)):
        if nlist[i] + nlist[x] == X:
            d1, d2 = nlist[i], nlist[x]
            break
            
nlist.remove(d1)
nlist.remove(d2)
nlist.sort()

for i in nlist:
    print(i)