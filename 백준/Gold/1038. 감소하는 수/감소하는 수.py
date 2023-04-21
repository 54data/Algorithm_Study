from itertools import combinations
N = int(input())
nlist = list(range(0, 10))
result = []

for i in range(1, 11):
    temp = list(combinations(nlist, i))
    temp = [int("".join(list(map(str, sorted(i, reverse=True))))) for i in temp]
    result.extend(temp)

result.sort()
if len(result) >= N+1:
    print(result[N])
else:
    print(-1)