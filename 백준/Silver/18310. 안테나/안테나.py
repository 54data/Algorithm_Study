n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
print(nlist[(n-1)//2])