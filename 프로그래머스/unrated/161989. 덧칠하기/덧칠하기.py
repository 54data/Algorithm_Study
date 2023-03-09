def solution(n, m, section):
    answer = 0
    idx = 0
    now = 0
    while idx < len(section) :
        if section[idx] > now:
            now = section[idx] + m - 1
            idx += 1
            answer += 1
            continue
        else:
            idx += 1
    return answer