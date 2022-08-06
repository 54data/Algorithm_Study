t = int(input())

for i in range(t):
    n = int(input())
    nlist = []

    while(n>0):
        nlist.append(n%2)
        n //= 2

    for i in range(len(nlist)):
        if nlist[i] == 1:
            print(i, end=' ')