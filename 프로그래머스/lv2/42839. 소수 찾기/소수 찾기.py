def sosu(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return 1
    
def solution(numbers):
    from itertools import permutations as pm
    result = []
    for i in range(1, len(numbers)+1):
        result.extend(list(pm(numbers, i)))
    
    result = [int(''.join(i)) for i in result]
    result = list(set(result))
    
    cnt = 0
    for j in result:
        cnt += sosu(j)
        
    return cnt