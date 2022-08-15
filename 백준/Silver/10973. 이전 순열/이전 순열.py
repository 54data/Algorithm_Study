n = int(input())
nlist = list(range(1, n+1))
a = list(map(int, input().split()))
result = False
if nlist == a:
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            for j in range(n-1, 0, -1):
                if a[i-1] > a[j]:
                    a[i-1], a[j] = a[j], a[i-1]
                    a = a[:i] + sorted(a[i:], reverse=True)
                    result = True
                    break
        if result == True:
            for i in a:
                print(i, end=' ')
            break