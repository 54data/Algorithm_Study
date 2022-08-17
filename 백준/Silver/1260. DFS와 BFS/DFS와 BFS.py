n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[v] = True

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
graph = list(map(lambda x:sorted(x), graph))

result = []
result.append(str(v))
def dfs(graph, start, visited):
    global result
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            result.append(str(i))
            dfs(graph, i, visited)
    else:
        return
dfs(graph, v, visited)
print(' '.join(result))

visited = [False] * (n+1)
visited[v] = True
result = []
result.append(str(v))

from collections import deque
def bfs(graph, start, visited):
    global result
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                result.append(str(i))
                queue.append(i)
                
bfs(graph, v, visited)
print(' '.join(result))