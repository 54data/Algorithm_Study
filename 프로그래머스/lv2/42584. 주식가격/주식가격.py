from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    result = [0] * len(prices)
    cnt = 0
    while queue:
        x = queue.popleft()
        for i in queue:
            if i >= x:
                result[cnt] += 1
            else:
                result[cnt] += 1
                break
        cnt += 1
    result[-1] = 0
    return result

print(solution([1, 2, 3, 2, 3, 3, 1]))

