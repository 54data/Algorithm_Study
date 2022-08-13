def turn(graph):
    turn_list = [] 
    for i in range(len(graph[0])):
        turn_list.append(list(map(lambda x:x[i], graph))[::-1])

    return turn_list

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for rotation in range(4):
        key = turn(key)
        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
    