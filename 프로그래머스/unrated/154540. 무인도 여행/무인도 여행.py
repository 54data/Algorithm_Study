from collections import deque

def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    direction = [(1,0),(-1,0),(0,-1),(0,1)]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = True
                queue = deque([(i, j)])
                num = int(maps[i][j])
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny]:
                            if maps[nx][ny] != 'X':
                                num += int(maps[nx][ny])
                                visited[nx][ny] = True
                                queue.append((nx,ny))
                answer.append(num)

    if answer:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer