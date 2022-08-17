def solution(brown, yellow):
    for i in range(1, brown):
        x = (brown+yellow) // i
        if x*i == 2*x + 2*i - 4 +  yellow:
            return [x, i]