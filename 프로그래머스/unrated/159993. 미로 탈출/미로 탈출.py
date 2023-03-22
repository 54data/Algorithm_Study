from collections import deque
def bfs(maps, start):
    x, y = start
    q = deque([[x, y, 0]])
    
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    lever = False
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y, cnt = q.popleft()
        if lever and maps[x][y] == 'E':
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    if maps[nx][ny] == 'L':
                        q = deque()
                        visited = [[False] * m for _ in range(n)]
                        lever = True
                        visited[nx][ny] = True
                        q.append([nx, ny, cnt+1])
                        break
                    else:
                        visited[nx][ny] = True
                        q.append([nx, ny, cnt+1])

def solution(maps):
    global n, m
    n, m = len(maps), len(maps[0])
    
    start = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = [i, j]
    
    answer = bfs(maps, start)    
    return answer if answer is not None else -1
     