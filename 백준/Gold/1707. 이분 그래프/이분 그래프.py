import sys
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(v):
        for x in graph[v]:
            if visited[x] == 0:
                if visited[v] == 1:
                    visited[x] = 2
                elif visited[v] == 2:
                    visited[x] = 1
                result = dfs(x)
                if not result:
                    return False
            elif visited[v] == visited[x]:
                return False
        return True
    
    result = True
    
    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            result = dfs(i)
            if not result:
                break
    
    print('YES') if result == True else print('NO')