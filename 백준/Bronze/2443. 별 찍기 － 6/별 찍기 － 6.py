n = int(input())
n2 = 2*n-1
for i in range(n2, 0, -2):
    print(' '*((n2-i)//2) + '*'*i)