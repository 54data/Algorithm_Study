def solution(s):
    slist = list(map(int, sorted(s.split(' '))))
    return str(min(slist)) + ' ' + str(max(slist))