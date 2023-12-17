def solution(array, n):
    answer = sum([1 for x in array if x == n])
    return answer