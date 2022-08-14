def turn(graph):
    turn_list = []
    for i in range(len(graph[0])):
        turn_list.append(list(map(lambda x:x[i], graph))[::-1])
        
    return turn_list

def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if new_lock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    new_lock = []
    n = len(lock)
    m = len(key)
    for i in range(n*3):
        new_lock.append([])
        for j in range(n*3):
            new_lock[i].append(0)
    
    for i in range(n, n*2):
        for j in range(n, n*2):
            new_lock[i][j] = lock[i-n][j-n]
            
    for rotation in range(4):
        key = turn(key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                
                if check(new_lock) == True:
                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    return False