def solution(s):
    answer = len(s)
    
    for step in range(1, (len(s)//2)+1):
        x = s[:step]
        result = ''
        cnt = 1
        
        for j in range(step, len(s), step):
            if x == s[j:j+step]:
                cnt += 1
            else:
                result += str(cnt) + x if cnt >= 2 else x
                x = s[j:j+step]
                cnt = 1
                
        result += str(cnt) + x if cnt >= 2 else x
        
        answer = min(len(result), answer)
    return answer