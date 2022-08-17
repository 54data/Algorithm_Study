from itertools import permutations as pm
def solution(k, dungeons):
    answer = -1
    pmlist = list(pm(dungeons))
    result = []
    for i in pmlist:
        a = k
        cnt = 0
        for j in i:
            if j[0] <= a:
                a -= j[1]
                cnt += 1
            else:
                break
        result.append(cnt)
    return max(result)