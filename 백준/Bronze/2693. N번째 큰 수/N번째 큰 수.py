mlist = []
case = int(input())
for i in range(case):
    a = sorted(list(map(int, input().split())), reverse=True)
    mlist.append(a[2])
    
for i in mlist:
    print(i)