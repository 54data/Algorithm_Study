import heapq

n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
    
result = 0

if len(heap) >= 2:
    while(len(heap) != 1):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum_ab = a + b
        result += sum_ab
        heapq.heappush(heap, sum_ab)

    print(result)
else:
    print(0)