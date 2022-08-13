answer = 0
def dfs(max_len, cnt, result, numbers, target):
    global answer
    if cnt == max_len:
        if result == target:
            answer += 1
        return
    dfs(max_len, cnt+1, result+numbers[cnt], numbers, target)
    dfs(max_len, cnt+1, result-numbers[cnt], numbers, target)
    
def solution(numbers, target):
    global answer
    max_len = len(numbers)
    cnt = 0
    dfs(max_len, cnt,  0, numbers, target)
    return answer