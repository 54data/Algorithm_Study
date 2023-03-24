def solution(arr):
    answer = [0, 0]
    
    def search(x, y, n):
        start = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != start:
                    nn = n//2
                    search(x, y, nn)
                    search(x+nn, y, nn)
                    search(x, y+nn, nn)
                    search(x+nn, y+nn, nn)
                    return
        answer[start] += 1
            
    search(0, 0, len(arr))
    return answer