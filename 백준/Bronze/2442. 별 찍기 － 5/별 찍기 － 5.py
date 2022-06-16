n = int(input())
n2 = 2 * n - 1
for i in range(1, n2+1, 2):
    print(' '*((n2-i)//2) + '*'*i)