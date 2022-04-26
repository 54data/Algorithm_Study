n = int(input())
n = 2*n-1
for i in range(n):
    if i % 2 == 0:
        print(' '*(i//2)+'*'*(n-i))

for x in range(2, n+1):
    if x % 2 == 1:
        print(' '*((n-x)//2)+'*'*x)