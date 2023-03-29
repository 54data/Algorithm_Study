nlist = []
man = 0
for i in range(10):
    a = list(map(int, input().split()))
    man += a[1] - a[0]
    nlist.append(man)
    
print(max(nlist))