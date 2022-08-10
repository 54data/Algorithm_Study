def solution(k, dungeons):
    from itertools import permutations as pm
    dlist = list(pm(dungeons))
    answer = []
    
    for i in dlist:
        cnt = 0
        new_k = k
        for j in i:
            if (j[0] <= new_k) and (new_k - j[1] >= 0):
                new_k -= j[1]
                cnt += 1
            else:
                break
        answer.append(cnt)
            
    return max(answer)