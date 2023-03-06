def solution(n, s):
    if s < n:
        return [-1]
    
    q, r = divmod(s, n)
    answer = [q] * n
    
    idx = n-1
    for i in range(r):
        answer[idx-i] += 1
    return answer