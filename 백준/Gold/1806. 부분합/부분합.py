N, S = map(int, input().split())
nlist = list(map(int, input().split()))

answer =  N + 1
s = 0
e = 0
sum_value = nlist[0]

while s <= e:
    if sum_value >= S:
        answer = min(e-s+1, answer)
        sum_value -= nlist[s]
        s += 1
    else:
        e += 1
        if e < N:
            sum_value += nlist[e]
        else:
            break

if answer != N + 1:
    print(answer)
else:
    print(0)