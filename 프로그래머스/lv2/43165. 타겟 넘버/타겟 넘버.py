def dfs(n, numbers, target, result):
    global answer
    if n == len(numbers):
        if result == target:
            answer += 1
        return 
    else:
        dfs(n+1, numbers, target, result+numbers[n])
        dfs(n+1, numbers, target, result-numbers[n])
        
def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    dfs(0, numbers, target, 0)
    
    return answer