from itertools import combinations as cb
n, m = map(int, input().split())
nlist = list(range(1, n+1))
for i in list(cb(nlist, m)):
    print(' '.join(list(map(lambda x:str(x), list(i)))))