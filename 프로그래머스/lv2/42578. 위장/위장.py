from collections import defaultdict
def solution(clothes):
    answer = defaultdict(list)
    for i in clothes:
        answer[i[1]].append(i[0])
        
    cnt = 1
    for i in answer.keys():
        cnt *= (len(answer[i])+1)
    
    return cnt-1