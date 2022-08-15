def solution(n):
    cnt = 0
    for i in range(1, n+1):
        start = i
        sum_ = 0
        while True:
            if sum_ == n:
                cnt += 1
                break
            elif sum_ > n:
                break
            sum_ += i
            i += 1
    return cnt