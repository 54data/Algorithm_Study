n, k = map(int, input().split())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

nlist.sort()
dp = [10001] * (k+1)
dp[0] = 0

for i in range(k+1):
    for j in nlist:
        if i < j :
            break  
        dp[i] = min(dp[i], dp[i-j]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])