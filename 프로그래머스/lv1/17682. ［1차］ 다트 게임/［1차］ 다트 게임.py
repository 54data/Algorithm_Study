def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')
    bonus = {'S':1, 'D':2, 'T':3}
    result = []
    
    for i in dartResult:
        if (i.isdigit()) or i=='A':
            result.append(10 if i=='A' else int(i))
        elif i in ('S', 'D', 'T'):
            num = result.pop()
            result.append(num ** bonus[i])
        elif i == '#':
            result[-1] *= -1
        elif i == '*':
            num = result.pop()
            if len(result):
                result[-1] *= 2
            result.append(num*2)
            
    return sum(result)