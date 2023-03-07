from itertools import permutations
import copy
import re

def solution(expression):
    answer = 0
    chars = list(permutations(['+', '-', '*']))
    for char in chars:
        exp = copy.deepcopy(expression)
        ex = re.split('(\D)', exp)
        for c in char:
            while c in ex:
                idx = ex.index(c)
                ex[idx-1] = str(eval(''.join(ex[idx-1:idx+2])))
                del ex[idx]
                del ex[idx]
        answer = max(answer, abs(int(ex[0])))
                     
    return answer
        
        