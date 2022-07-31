def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i != ' ':
            if cnt % 2 == 0: answer += i.upper()
            else: answer += i.lower()
            cnt += 1
        else:
            answer += ' '
            cnt = 0
    return answer
                        