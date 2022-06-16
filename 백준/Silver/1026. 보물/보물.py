N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
while True:
    sum += (min(a) * max(b))
    a.remove(min(a))
    b.remove(max(b))
    if a == []:
        break
        
print(sum)