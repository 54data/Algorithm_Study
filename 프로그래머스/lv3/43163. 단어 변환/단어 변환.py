from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, answer))
    result = False
    while queue:
        x, answer = queue.popleft()
        if x == target:
            result = True
            break
        else:
            for i in words:
                cnt = 0
                for a, b in zip(i, x):
                    if a == b:
                        cnt += 1
                if len(target) -1 <= cnt < len(target):
                    words.remove(i)
                    queue.append((i, answer+1))
                    
    return answer if result == True else 0