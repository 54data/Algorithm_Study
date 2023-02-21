from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    topping1 = dict(Counter(topping))
    topping2 = defaultdict(int)
    
    topping1_cnt = len(topping1)
    topping2_cnt = 0
    
    for t in topping:
        topping2[t] += 1
        if topping2[t] == 1:
            topping2_cnt += 1
        
        topping1[t] -= 1
        if topping1[t] == 0:
            topping1_cnt -= 1
            del topping1[t]
            
        if topping1_cnt == topping2_cnt:
            answer += 1
            
    return answer