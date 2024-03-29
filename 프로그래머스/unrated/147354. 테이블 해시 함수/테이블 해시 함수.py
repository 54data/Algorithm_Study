def solution(data, col, row_begin, row_end):
    answer = []
    data = sorted(data, key=lambda x:[x[col-1], -x[0]])
    
    for i in range(row_begin, row_end+1):
        result = 0
        for j in data[i-1]:
            result += j % i
        if not answer:
            answer.append(result)
        else:
            answer[0] ^= result
    return answer[0]