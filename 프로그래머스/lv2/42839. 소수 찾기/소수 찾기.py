def sosu(x):
    sosu_list = []
    for i in x:
        if i == 1 or i == 0:
            pass
        else:
            for j in range(2, int(i**0.5)+1):
                if i!=j and i%j==0:
                    break
            else:
                sosu_list.append(i)
    return len(sosu_list)

from itertools import permutations as pm
def solution(numbers):
    result = []
    for i in range(1, len(numbers)+1):
        result += list(pm(list(numbers), i))
    result = list(map(lambda x:int(''.join(x)), result))
    result = list(set(result))
    result.sort()
    return sosu(result)