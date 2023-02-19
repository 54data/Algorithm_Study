from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    queue = deque()
    for i in range(len(numbers)):
        temp = numbers[i]
        while queue and queue[0][0] < temp:
            _, idx = queue.popleft()
            answer[idx] = temp
        queue.appendleft([temp, i])
    return answer