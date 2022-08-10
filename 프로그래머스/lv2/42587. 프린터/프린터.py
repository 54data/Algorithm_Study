def solution(priorities, location):
    answer = []
    array = [(i, x) for i, x in enumerate(priorities)]
    while (array != []):
        if array[0][1] < max(array, key=lambda x:x[1])[1]:
            array.append(array.pop(0))
        else:
            answer.append(array.pop(0)[0])
    return answer.index(location) + 1
            
