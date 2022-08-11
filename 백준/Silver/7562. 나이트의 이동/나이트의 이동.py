from collections import deque
import sys

case = int(sys.stdin.readline())

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

for _ in range(case):
    n = int(sys.stdin.readline())
    graph = [[0]*n for _ in range(n)] 
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())
        
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 1
    
    while queue:
        x, y = queue.popleft()
        if (x == end_x) and (y == end_y):
            print(graph[x][y]-1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))