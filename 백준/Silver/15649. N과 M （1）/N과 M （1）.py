from itertools import permutations as pm
n, m = map(int, input().split())
nlist = list(range(1, n+1))
for i in list(pm(nlist, m)):
    print(' '.join(list(map(lambda x:str(x), list(i)))))