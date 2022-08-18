n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))
    
for i in nlist:
    cnt = 0
    for j in nlist:
        if j[0] > i[0] and j[1] > i[1]:
            cnt += 1
    print(cnt+1, end=' ')