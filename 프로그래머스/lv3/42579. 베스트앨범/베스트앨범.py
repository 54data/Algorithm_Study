def solution(genres, plays):
    result = {}
    for i in genres:
        result[i] = 0
        
    for i,x in zip(genres, plays):
        result[i] += x
        
    keylist = list(result.keys())
    keylist.sort(key=lambda x:result[x], reverse=True)
    
    answer = []
    for i in keylist:
        append_list = []
        for x in range(len(genres)):
            if genres[x] == i:
                append_list.append([x, plays[x]])
        append_list.sort(key=lambda x:x[1], reverse=True)
        answer.append(append_list[0][0])
        if len(append_list) > 1:
            answer.append(append_list[1][0])
        
    return answer