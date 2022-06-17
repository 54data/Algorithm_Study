n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in num:
    if i == n:
        cnt += 1
        
print(cnt)