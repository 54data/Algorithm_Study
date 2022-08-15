from itertools import combinations as cb
n, s = map(int, input().split())
nlist = list(map(int, input().split()))

answer = 0
for i in range(1, n+1):
    for j in list(cb(nlist, i)):
        if sum(j) == s:
            answer += 1
            
print(answer)