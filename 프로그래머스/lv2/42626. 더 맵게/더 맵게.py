import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville:
        if len(scoville) <= 1:
            return -1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x+y*2)
        cnt += 1
        for i in scoville:
            if i < K:
                break
        else:
            return cnt