def fac(n):
    answer = 1
    for i in range(1, n):
        answer *= i
    return answer

def solution(n, k):
    result = []
    nlist = list(range(1, n+1))
    
    while n!=0:
        temp = fac(n)
        index = k // temp
        k %= temp
        if k == 0:
            result.append(nlist.pop(index-1))
        else:
            result.append(nlist.pop(index))
        n -= 1
        
    return result