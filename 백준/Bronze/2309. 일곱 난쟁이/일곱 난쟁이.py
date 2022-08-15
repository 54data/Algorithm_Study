from itertools import combinations as cb
nlist = [int(input()) for _ in range(9)]
seven = list(cb(nlist, 7))

for i in seven:
    if sum(i) == 100:
        for j in sorted(list(i)):
            print(j)
        break