from collections import defaultdict
from collections import deque

def bfs(i, j, n, graph, wires):
    cnt = 0
    visited = [False] * (n+1)
    q = deque([i])
    visited[i] = True
    
    while q:
        x = q.popleft()
        for y in graph[x]:
            if y == j:
                continue
            if visited[y]:
                continue
            cnt += 1
            q.append(y)
            visited[y] = True
    return cnt
    
def solution(n, wires):
    answer = 1e9
    graph = defaultdict(list)
    for x in wires:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])
        
    for x in wires:
        i, j = x[0], x[1]
        temp = abs(bfs(i, j, n, graph, wires) - bfs(j, i, n, graph, wires))
        answer = min(answer, temp)
        
    return answer