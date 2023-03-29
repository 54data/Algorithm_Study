# 2581
m = int(input())
n = int(input())
cnt2 = 0
result = []
for i in range(m, n+1):
    cnt = 0
    for x in range(1, i+1):
        if (i%x == 0) and (i!=1):
            if (x==1) or (x==i):
                cnt += 1
            else:
                cnt = 0
    if cnt==2:
        result.append(i)
        
if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)