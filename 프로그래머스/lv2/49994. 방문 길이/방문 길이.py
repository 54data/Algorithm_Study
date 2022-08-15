def solution(dirs):
    dx = [-1, 1, 0, 0] # U, D
    dy = [0, 0, -1, 1] # L, R
    xy = ['U', 'D', 'L', 'R']
    
    graph = [[0]*11 for _ in range(0, 11)]
    graph[5][5] = 1
    visited = []
    
    x, y = 5, 5
    cnt = 0
    for i in dirs:
        nx = dx[xy.index(i)]+x
        ny = dy[xy.index(i)]+y
        if nx<0 or ny<0 or nx>10 or ny>10:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            if (x, y, nx, ny) not in visited:
                visited.append((x, y, nx, ny))
                x, y = nx, ny
                cnt += 1
        elif graph[nx][ny] == 1 and (x, y, nx, ny) not in visited:
            if (nx, ny, x, y) in visited:
                pass
            else:
                visited.append((x, y, nx, ny))
                cnt += 1
        x, y = nx, ny
        
    return cnt