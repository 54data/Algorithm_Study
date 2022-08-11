n, m = map(int, input().split())
graph = [[] for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * n

ans = False
def dfs(v, cnt):
    global ans
    visited[v] = True
    
    if cnt == 4:
        ans = True
        return 
    for i in graph[v]:
        if visited[i] == False:
            dfs(i, cnt+1)
            visited[i] = False
            
for j in range(n):
    dfs(j, 0)
    visited[j] = False
    if ans:
        break
    
print(1 if ans else 0)