from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    while (q1 and q2):
        if answer > 300000*2:
            return -1
        if sum_queue1 == sum_queue2:
            return answer
        elif sum_queue1 > sum_queue2:
            temp = q1.popleft()
            sum_queue1 -= temp
            sum_queue2 += temp
            q2.append(temp)
            answer += 1
        elif sum_queue1 < sum_queue2:
            temp = q2.popleft()
            sum_queue1 += temp
            sum_queue2 -= temp
            q1.append(temp)
            answer += 1
    else:
        return -1
            
    return answer