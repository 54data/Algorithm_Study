import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

cnt = 0
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
    
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)