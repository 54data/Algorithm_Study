import sys
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)]

# 최대 개수 체크
def check(graph, x, y, nx, ny):
    row_max, col_max = -1e9, -1e9
    for i in range(n):
        row_cnt = 1
        col_cnt = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
            if graph[j][i] == graph[j+1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        
    return max(row_max, col_max)

# 인접한 두 칸 교환
def change(n, graph):
    max_result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(n):
            for x in range(4):
                nx = dx[x]+i
                ny = dy[x]+j
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                else:
                    if graph[i][j] != graph[nx][ny]:
                        graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
                        max_result = max(max_result, check(graph, i, j, nx, ny))
                        graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
                        
    return max_result

print(change(n, graph))