def solution(sizes):
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
    max_a = sorted(sizes, key=lambda x:x[0], reverse=True)[0][0]
    max_b = sorted(sizes, key=lambda x:x[1], reverse=True)[0][1]
    return max_a * max_b
