def solution(s):
    new_s = s.replace(' ', '!')
    answer = ''
    
    cnt = 0
    for i in new_s:
        if i == '!':
            answer += ' '
            cnt = 0
            continue
        if cnt == 0:
            if not i.isdigit():
                answer += i.upper()
            else:
                answer += i
            cnt = 1
            continue
        if cnt == 1:
            if not i.isdigit():
                answer += i.lower()
            else:
                answer += i
                
    return answer