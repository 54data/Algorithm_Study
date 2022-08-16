from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for x in course:
        temp = []
        for order in orders:
            cb = combinations(sorted(order), x)
            temp += cb
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(x) for x in counter if counter[x] == max(counter.values())]
    return sorted(answer)