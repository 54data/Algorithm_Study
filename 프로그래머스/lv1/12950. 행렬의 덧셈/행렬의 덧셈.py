def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        result = []
        for x, y in zip(i, j):
            result.append(x+y)
        answer.append(result)
    return answer