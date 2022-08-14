def check(n, x, queen):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x]-queen[i]) == abs(x-i):
            return False
    return True

def set_queen(n, x, queen):
    result = 0
    if x == n:
        return 1

    for i in range(n):
        queen[x] = i
        if check(n, x, queen):
            result += set_queen(n, x+1, queen)
    return result
            
                
def solution(n):
    queen = [0] * n
    return set_queen(n, 0, queen)