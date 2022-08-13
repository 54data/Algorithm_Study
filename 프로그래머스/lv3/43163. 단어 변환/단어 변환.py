from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, answer])
    result = False
    
    while queue:
        x, answer = queue.popleft()
        if x == target:
            result = True
            break
        for i in words:
            cnt = 0
            for a, b in zip(x, i):
                if a == b:
                    cnt += 1
            if len(x) > cnt >= len(x)-1:
                words.remove(i)
                queue.append([i, answer+1])
            
    return answer if result != False else 0