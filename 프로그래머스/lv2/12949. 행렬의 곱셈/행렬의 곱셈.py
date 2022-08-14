def solution(arr1, arr2):
    answer = []
    new_arr2 = []
    for i in range(len(arr2[0])):
        new_arr2.append(list(map(lambda x:x[i], arr2)))
    
    for i in arr1:
        result = []
        for j in new_arr2:
            sum = 0
            for x in range(len(i)):
                sum += i[x] * j[x]
            result.append(sum)
        answer.append(result)
        
    return answer            