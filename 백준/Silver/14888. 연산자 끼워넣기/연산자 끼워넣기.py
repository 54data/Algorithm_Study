import sys

n = int(input())
nlist = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
result = nlist[0]

max_num = -(sys.maxsize)
min_num = sys.maxsize

def dfs(cnt, result, plus, minus, mul, div):
    global max_num, min_num
    if cnt == n:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
        
    if plus > 0:
        dfs(cnt+1, result+nlist[cnt], plus-1, minus, mul, div)
    if minus > 0:
        dfs(cnt+1, result-nlist[cnt], plus, minus-1, mul, div)
    if mul > 0:
        dfs(cnt+1, result*nlist[cnt], plus, minus, mul-1, div)
    if div > 0:
        dfs(cnt+1, int(result/nlist[cnt]), plus, minus, mul, div-1)
        
dfs(1, result, plus, minus, mul, div)
print(max_num)
print(min_num)