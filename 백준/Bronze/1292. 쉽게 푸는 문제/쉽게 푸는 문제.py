a, b = map(int, input().split())
result = [0]

for i in range(1, b+1):
    for x in range(i):
        result.append(i)
        
print(sum(result[a:b+1]))