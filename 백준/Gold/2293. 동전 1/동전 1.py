n, k = map(int, input().split())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for i in nlist:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])