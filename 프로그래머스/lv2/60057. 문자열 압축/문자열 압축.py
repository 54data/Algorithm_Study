def solution(s):
    answer = len(s)

    for i in range(1, (len(s)//2)+1):
        result = ''
        start = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if start == s[j:i+j]:
                cnt += 1
            else:
                result += str(cnt) + start if cnt>1 else start
                start = s[j:i+j]
                cnt = 1
        result += str(cnt) + start if cnt>1 else start
        answer = min(len(result), answer)

    return answer