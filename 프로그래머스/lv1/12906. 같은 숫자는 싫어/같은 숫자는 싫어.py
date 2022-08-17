def solution(arr):
    a = [arr[0]]
    for i in arr[1:]:
        if i != a[-1]:
            a.append(i)
    return a