from collections import defaultdict
import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = defaultdict(list)
dist = defaultdict(int)

for _ in range(M):
    ss, ee, cost = map(int, sys.stdin.readline().split())
    graph[ss].append((cost, ee))

s, e = map(int, sys.stdin.readline().split())
queue = [[0, s]]

while queue:
    cost, node = heapq.heappop(queue)
    if node not in dist:
        dist[node] = cost
        for w, v in graph[node]:
            temp = cost + w
            heapq.heappush(queue, [temp, v])

print(dist[e])