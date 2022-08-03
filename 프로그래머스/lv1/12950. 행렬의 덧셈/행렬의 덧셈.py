def solution(arr1, arr2):
    answer = []
    for i, x in zip(arr1, arr2):
        sum_result = []
        for y, z in zip(i, x):
            sum_result.append(y+z)
        answer.append(sum_result)
    return answer