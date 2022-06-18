n = int(input())
result = [0, 1]
for i in range(2, n+1):
    num = result[i-1] + result[i-2]
    result.append(num)
    
print(result[n])