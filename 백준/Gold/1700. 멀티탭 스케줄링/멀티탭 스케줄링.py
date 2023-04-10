N, K = map(int, input().split())
nlist = list(map(int, input().split()))
mul = []
cnt = 0

for i in range(K):
    if len(mul) < N and nlist[i] not in mul:
        mul.append(nlist[i])
    elif nlist[i] in mul:
        continue
    else:
        find_max_plug = 0
        change_status = True
        for idx in range(len(mul)):
            if mul[idx] not in nlist[i:]:
                mul[idx] = nlist[i]
                cnt += 1
                change_status = False
                break
            else:
                if find_max_plug <= nlist[i:].index(mul[idx]):
                    find_max_plug = nlist[i:].index(mul[idx])
                    change_idx = idx
        if change_status and find_max_plug != 0:
            mul[change_idx] = nlist[i]
            cnt += 1

print(cnt)