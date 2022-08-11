from collections import deque

n, m = map(int, input().split())
graph = [0] * 100001
path = [0] * 100001
        
def move(x):
    path_list = []
    temp = x
    for _ in range(graph[x]+1):
        path_list.append(temp)
        temp = path[temp]
    print(' '.join(map(str, path_list[::-1])))
    
def bfs():
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        if x == m:
            print(graph[m])
            move(x)
            return
        for dx in (x-1, x+1, x*2):
            if (0<= dx <=100000) and (graph[dx] == 0):
                graph[dx] = graph[x] + 1
                queue.append(dx)
                path[dx] = x
                
bfs()