n = int(input())
n2 = 2*n
for i in range(1, n2, 2):
    print(' '*((n2-i)//2) + '*'*i)
for i in range(n2-3, 0, -2):
    print(' '*((n2-i)//2) + '*'*i)