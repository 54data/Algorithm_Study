def solution(N, stages):
    users = len(stages)
    result = []
    for i in range(1, N+1):
        if users <= 0:
            result.append([i, 0])
        else:
            result.append([i, stages.count(i) / users])
            users -= stages.count(i)
            
    result.sort(reverse=True, key=lambda x:(x[1], -x[0]))
    return list(map(lambda x:x[0], result))