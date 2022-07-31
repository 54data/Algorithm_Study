def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        for i in s:
            if i.isnumeric() == False:
                answer = False
                break
            else: answer = True
    else: answer = False
    return answer