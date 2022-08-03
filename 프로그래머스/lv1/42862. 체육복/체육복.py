def solution(n, lost, reserve):
    rlist = sorted([r for r in reserve if r not in lost])
    llist = sorted([l for l in lost if l not in reserve])
    
    for r in rlist:
        f = r - 1
        b = r + 1
        if f in llist:
            llist.remove(f)
        elif b in llist:
            llist.remove(b)
    return n - len(llist)