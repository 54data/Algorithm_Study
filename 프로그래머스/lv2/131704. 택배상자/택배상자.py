def solution(order):
    sub = []
    i = 1
    answer = 0
    
    while True:
        if i == len(order) + 1:
            break
        sub.append(i)
        while sub and sub[-1] == order[answer]:
            answer += 1
            sub.pop(-1)
        i += 1
    return answer