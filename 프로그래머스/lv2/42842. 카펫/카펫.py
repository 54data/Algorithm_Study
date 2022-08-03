def solution(brown, yellow):
    for x in range(2, int(brown/2)+1):
        y = (brown+4)/2 - x
        if (x*y == brown + yellow) and (x>=y):
            return [x, y]