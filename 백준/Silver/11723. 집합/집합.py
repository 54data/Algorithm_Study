import sys
s = set()
m = int(sys.stdin.readline())
for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    if temp[0] == 'add':
        if int(temp[1]) not in s:
            s.add(int(temp[1]))
            continue
    if temp[0] == 'remove':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
        continue
    if temp[0] == 'check':
        print(list(s).count(int(temp[1])))
        continue
    if temp[0] == 'toggle':
        if int(temp[1]) in s:
            s.remove(int(temp[1]))
        else:
            s.add(int(temp[1]))
        continue
    if temp[0] == 'all':
        s = set(list(range(1, 21)))
        continue
    if temp[0] == 'empty':
        s = set()