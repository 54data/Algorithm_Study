from collections import deque

def bfs(maps, queue, visited, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
    return visited[n-1][m-1]
    
def solution(maps):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    answer = bfs(maps, queue, visited, n, m)
    return answer if answer != 0 else -1