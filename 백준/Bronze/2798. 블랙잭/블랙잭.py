from itertools import combinations as cb
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
result = list(cb(nlist, 3))

cnt = 0
for i in result:
    if sum(i) <= m:
        cnt = max(cnt, sum(i))
    
print(cnt)