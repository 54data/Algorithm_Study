def solution(n, arr1, arr2):
    map1, map2 = [], []
    for _ in range(n):
        map1.append([])
        map2.append([])
        
    for i in range(len(arr1)):
        for x in range(n):
            map1[i].insert(0, arr1[i] % 2)
            map2[i].insert(0, arr2[i] % 2)
            arr1[i] //= 2
            arr2[i] //= 2
            
    answer = []
    for x, y in zip(map1, map2):
        result = ''
        for a, b in zip(x, y):
            if (a==1) or (b==1): result += '#'
            else: result += ' '
        answer.append(result)
    return answer