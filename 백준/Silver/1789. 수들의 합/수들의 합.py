n = int(input())
result = 0
cnt = 0
for i in range(1, n+1):
    result += i
    cnt += 1
    if result > n:
        cnt -= 1
        break
    elif result == n:
        break
        
print(cnt)