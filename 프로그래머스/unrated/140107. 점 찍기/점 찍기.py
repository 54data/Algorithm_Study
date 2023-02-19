import math
def solution(k, d):
    answer = 0
    
    for i in range(0, d+1):
        x = i*k
        if d**2 - x**2 >= 0:
            y = int(math.sqrt(d**2 - x**2)) // k
            answer += (y+1)
    
    return answer