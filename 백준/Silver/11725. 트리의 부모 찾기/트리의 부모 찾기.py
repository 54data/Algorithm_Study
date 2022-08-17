import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
            
def dfs(start, graph, parents):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, graph, parents)
        
dfs(1, graph, parents)

for i in range(2, n+1):
    print(parents[i])