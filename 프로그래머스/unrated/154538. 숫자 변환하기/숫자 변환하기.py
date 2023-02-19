from collections import deque

def solution(x, y, n):
    answer = 0
    queue = deque([(y, 0)])
    
    while queue:
        num, cnt = queue.popleft()
        if num < 1:
            return -1
        if num == x:
            return cnt
        if num % 3 == 0:
            queue.append((num//3, cnt+1))
        if num % 2 == 0:
            queue.append((num//2, cnt+1))
        queue.append((num-n, cnt+1))
            
        
        