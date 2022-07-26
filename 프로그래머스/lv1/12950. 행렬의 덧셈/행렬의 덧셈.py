def solution(arr1, arr2):
    answer = []
    for i, x in zip(arr1, arr2):
        answer2 = []
        for z, y in zip(i, x):
            answer2.append(z+y)
        answer.append(answer2)
    return answer