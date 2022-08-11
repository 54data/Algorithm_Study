from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        else:
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

answer = True
day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = False
            break
        else:
            day = max(day, graph[i][j])
            
print(day-1) if answer == True else print(-1)