n = int(input())
a = []
for i in range(n):
    a.append(input().split())

for i in range(len(a)):
    print('Case #{}: {}'.format(i+1, ' '.join(a[i][::-1])))