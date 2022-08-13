from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())

graph = [-1] * 100001
queue = deque()
queue.append(n)
graph[n] = 0

while queue:
    x = queue.popleft()
    if x==k:
        print(graph[x])
        break
    for i in [2*x, x-1, x+1]:
        if 0<= i <100001 and graph[i] == -1:
            if i == 2*x:
                graph[i] = graph[x]
                queue.appendleft(i)
            else:
                graph[i] = graph[x] + 1
                queue.append(i)