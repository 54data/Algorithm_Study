def solution(operations):
    answer = []
    for i in operations:
        if i[0] == 'I':
            answer.append(int(i[i.find(' ')+1:]))
            answer.sort()
        elif answer != []:
            if '-' in i: del answer[0]
            else: del answer[-1]
    return [0, 0] if answer == [] else [max(answer), min(answer)]