def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        arr[i+1] = min_common(arr[i], arr[i+1])
        
    return arr[-1]

def min_common(x, y):
    gob = x*y
    x, y = max(x, y), min(x, y)
    while(y!=0):
        r = x % y
        x, y = y, r
    
    return gob // x
    