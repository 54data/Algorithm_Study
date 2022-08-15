n = int(input())
nlist = list(range(1, n+1))
a = list(map(int, input().split()))
result = False
if a == nlist[::-1]:
    print(-1)
else:
    change = False
    for i in range(n-1, 0, -1):
        if a[i-1] < a[i]:
            for j in range(n-1, 0, -1):
                if a[i-1] < a[j]:
                    a[i-1], a[j] = a[j], a[i-1]
                    a = a[:i] + sorted(a[i:])
                    result = True
                    break
        if result == True:
            break
    for i in a:
        print(i, end=' ')      