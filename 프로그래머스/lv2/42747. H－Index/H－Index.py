def solution(citations):
    answer = 0
    start = 0
    end = max(citations)
    while start<=end:
        mid = (start + end) // 2
        cnt = 0
        for i in citations:
            if i >= mid:
                cnt += 1   
        if cnt >= mid and len(citations) - cnt <= mid:
            answer = mid
        if cnt < mid:
            end = mid - 1
        else:
            start = mid + 1
    return answer