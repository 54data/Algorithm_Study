def solution(brown, yellow):
    c = brown + yellow
    result = []
    for i in range(2, c+1):
        if c % i == 0: result.append([c//i, i])
    for x in result:
        if 2 * (x[0] + x[1] - 2) == brown:
            answer_x, answer_y = max(x[0], x[1]), min(x[0], x[1])
            break
    return [answer_x, answer_y ]