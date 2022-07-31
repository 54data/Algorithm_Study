def solution(n):
    nlist = sorted(list(str(n)), reverse=True)
    answer = "".join(nlist)
    return int(answer)