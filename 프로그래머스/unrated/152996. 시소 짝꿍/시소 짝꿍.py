from collections import Counter

def solution(weights):
    answer = 0
    meters = [4/3, 2, 3/2]
    counter = Counter(weights)
    for k, v in counter.items():
        if v > 1:
            answer += v*(v-1) / 2
    
    weights = sorted(set(weights))
    for i in range(len(weights)):
        for m in meters:
            if weights[i] * m in weights:
                answer += counter[weights[i]*m] * counter[weights[i]]

    return answer
                