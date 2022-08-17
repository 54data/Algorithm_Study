result = 0
def dfs(cnt, numbers, target, answer):
    global result
    if cnt == len(numbers):
        if answer == target:
            result += 1
        else:
            return
    else:
        dfs(cnt+1, numbers, target, answer+numbers[cnt])
        dfs(cnt+1, numbers, target, answer-numbers[cnt])
    
def solution(numbers, target):
    global result
    answer = 0
    dfs(0, numbers, target, 0)
    
    return result