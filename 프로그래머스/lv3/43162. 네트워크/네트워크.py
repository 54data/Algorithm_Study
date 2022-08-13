def solution(n, computers):
    answer = 0
    def dfs(x, y):
        if computers[x][y] == 1:
            computers[x][y] = 0
            for i in range(n):
                if computers[x][i] == 1:
                    computers[x][i] = 0
                    dfs(i, x)
            return True
        return False
            
    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                answer += 1
    return answer