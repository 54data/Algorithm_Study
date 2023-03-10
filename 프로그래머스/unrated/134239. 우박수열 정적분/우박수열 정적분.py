def solution(k, ranges):
    klist = [k]
    answer = []
    while k != 1:
        if k % 2 == 0:
            k = k//2
        else:
            k = k*3 + 1
        klist.append(k)
        
    for i, j in ranges:
        if i - j >= len(klist):
            answer.append(-1.0)
        else:
            answer.append(sum(klist[i:len(klist)+j]) - (klist[i] + klist[len(klist)+j-1]) /2)
            
    return answer