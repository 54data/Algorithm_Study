import sys
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
set_list = sorted(list(set(nlist)))
dict1 = {set_list[i]:i for i in range(len(set_list))}
for i in nlist:
    print(dict1[i], end=' ')