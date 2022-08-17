def solution(progresses, speeds):
    answer = []
    cnt = 0
    while True:
        for i, x in enumerate(speeds):
            progresses[i] += x
            
        while True:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
                if progresses == []:
                    break
            else:
                break
                
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
            
        if speeds == []:
            break
            
    return answer