a, b = map(int, input().split())
nlist = [i for i in range(1, a+1) if a%i == 0]
if b-1 >= len(nlist) : print(0)
else: print(nlist[b-1])