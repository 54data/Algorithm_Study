T = int(input())
for i in range(T):
    result = list(range(1, 15))
    k = int(input())
    n = int(input())
    for _ in range(k):
        result2 = []
        for z in range(n):
            result2.append(sum(result[0:z+1]))
        result = result2
    print(result2[n-1])