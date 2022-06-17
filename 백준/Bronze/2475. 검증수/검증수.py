n = list(map(int, input().split()))
sum_result = 0
for i in n:
    sum_result += i**2
    
print(sum_result%10)