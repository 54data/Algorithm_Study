import heapq

heap = []
n = int(input())

for _ in range(n):
    num_list = map(int, input().split())
    for x in num_list:
        if len(heap) < n:
            heapq.heappush(heap, x)
        else:
            if heap[0] < x:
                heapq.heappop(heap)
                heapq.heappush(heap, x)
                
print(heap[0])