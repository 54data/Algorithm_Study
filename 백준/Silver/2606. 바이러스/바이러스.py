n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
graph = list(map(lambda x:sorted(x), graph))

visited = [False] * (n+1)

from collections import deque

cnt = 0
def bfs(graph, start, visited):
    queue = deque([start])
    global cnt
    while queue:
        v = queue.popleft()
        visited[v] = True
        
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                cnt += 1
    print(cnt)
                
bfs(graph, 1, visited)