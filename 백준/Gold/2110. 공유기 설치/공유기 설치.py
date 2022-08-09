import sys
n, c = map(int, input().split())
nlist = []
for i in range(n):
    nlist.append(int(sys.stdin.readline()))
    
nlist.sort() 

start = 1
end = nlist[-1] - nlist[0] 
result = 0

while(start <= end):
    mid = (start + end) // 2 
    value = nlist[0]
    count = 1
    for i in range(1, n):
        if nlist[i] >= value + mid: 
            value = nlist[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid -1
        
print(result)