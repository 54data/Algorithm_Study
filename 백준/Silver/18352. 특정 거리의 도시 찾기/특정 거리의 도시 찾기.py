from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
visited[x] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
queue = deque()
queue.append(x)
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)

answer = False
for i in range(1, n+1):
    if visited[i] == k:
        answer = True
        print(i)
if answer == False:
    print(-1)