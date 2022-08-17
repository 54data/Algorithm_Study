def check(answers, a):
    cnt = 0
    for x, y in zip(answers, a):
        if x==y:
            cnt += 1
    return cnt
def solution(answers):
    a1 = [1, 2, 3, 4, 5] * 2000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    
    result = []
    result.append(check(answers, a1))
    result.append(check(answers, a2))
    result.append(check(answers, a3))
    
    answer = []
    for i in range(len(result)):
        if result[i] == max(result):
            answer.append(i+1)
    return answer
