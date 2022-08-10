n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a = list(map(int, input().split()))
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])
    
graph = list(map(lambda x:sorted(x), graph))
visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, v, visited)

visited2 = [False] * (n+1)

print(end='\n')

from collections import deque

def bfs(graph, start, visited2):
    queue = deque([start])
    visited2[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited2[i] == False:
                queue.append(i)
                visited2[i] = True
                
bfs(graph, v, visited2)