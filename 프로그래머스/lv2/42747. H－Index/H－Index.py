def solution(citations):
    citations.sort()
    for i in range(max(citations), -1, -1):
        a = len(list(filter(lambda x:x>=i, citations)))
        if a >= i and len(citations) - a <= i:
            return i