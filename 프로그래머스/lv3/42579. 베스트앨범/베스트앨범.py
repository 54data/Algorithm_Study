from collections import defaultdict
def solution(genres, plays):
    temp = defaultdict(int)
    for i, j in zip(genres, plays):
        temp[i] += j
        
    result = []
    x = 0
    for i, j in zip(genres, plays):
        result.append((i, j, x))
        x += 1

    result.sort(key=lambda x:(temp[x[0]], x[1], -x[2]), reverse=True)        
    most_play = sorted(list(temp.keys()), key=lambda x:temp[x], reverse=True)
    
    answer = []
    for i in most_play:
        cnt = 0
        for j in result:
            if i == j[0]:
                if cnt < 2:
                    answer.append(j[2])
                    cnt += 1
            else:
                cnt = 0
                continue
    return answer
                