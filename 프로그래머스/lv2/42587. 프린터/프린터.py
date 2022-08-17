from collections import deque
def solution(priorities, location):
    result = []
    for i, j in enumerate(priorities):
        result.append((i, j))
    queue = deque(result)
    answer = []
    while queue:
        x, y= queue.popleft()
        for i in queue:
            if i[1] > y:
                queue.append((x, y))
                break
        else:
            answer.append((x, y))
    
    for i in range(len(answer)):
        if answer[i][0] == location:
            return i+1
                