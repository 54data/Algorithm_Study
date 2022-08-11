from collections import deque

n, k = map(int, input().split())
move = [-1, 1, 2]
graph = [0] * 100001
graph[n] = 1

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        break
    for i in move:
        if i != 2:
            dx = x + i
        else:
            dx = x * i
        if (dx >= 0) and (dx <= 100000):
            if graph[dx] == 0:
                graph[dx] = graph[x] + 1
                queue.append(dx)
                
print(graph[k]-1)