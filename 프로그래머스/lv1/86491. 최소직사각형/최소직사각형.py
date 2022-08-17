def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1], sizes[i][0]]

    return max(map(lambda x:x[0], sizes)) * max(map(lambda x:x[1], sizes))