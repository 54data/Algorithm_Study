def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, cnt, result):
    global answer
    if cnt == len(numbers):
        if result == target:
            answer += 1
        else:
            return
    else:
        dfs(numbers, target, cnt+1, result+numbers[cnt])
        dfs(numbers, target, cnt+1, result-numbers[cnt])
    