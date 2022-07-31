def solution(n):

    nlist = [True]*(n+1)

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if nlist[i] == True:
            for j in range(i+i, n+1, i):
                nlist[j] = False

    return len([i for i in range(2, n+1) if nlist[i] == True])
