def solution(elements):
    answer = []
    elem = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(elem[j:j+i+1]))
            
    return len(set(answer))
        