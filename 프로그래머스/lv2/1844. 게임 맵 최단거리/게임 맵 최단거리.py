from collections import deque
def bfs(x, y, maps, visited, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            else:
                if (maps[nx][ny] == 1) and (visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    return maps[n-1][m-1]
    
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    answer = bfs(0, 0, maps, visited, n, m)
    return answer if answer != 1 else -1