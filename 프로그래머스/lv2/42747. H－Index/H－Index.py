def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations), 0, -1):
        if len([x for x in citations if x >= i]) >= i:
            answer = i
            break
    return answer