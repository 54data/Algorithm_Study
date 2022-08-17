from itertools import permutations as pm
def sosu(x):
    if x == 0 or x == 1:
        return 0
    for i in range(2, int(x*0.5)+1):
        if x!=i and x%i==0:
            return 0
    else:
        return 1
        
def solution(numbers):
    result = []
    for i in range(1, len(numbers)+1):
        result += list(pm(list(numbers), i))
        
    result = list(map(lambda x:int(''.join(x)), result))
    result = list(set(result))
    result.sort()
    cnt = 0
    for i in result:
        cnt += sosu(i)
    return cnt