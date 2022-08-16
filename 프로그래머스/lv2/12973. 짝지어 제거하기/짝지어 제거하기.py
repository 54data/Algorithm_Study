def solution(s):
    if len(s) % 2 == 1:
        return 0
    slist = list(s)
    poplist = []
    for i in slist:
        poplist.append(i)
        if len(poplist)>=2 and poplist[-1] == poplist[-2]:
            poplist.pop(-1)
            poplist.pop(-1)
            
    if poplist != []:
        return 0
    else:
        return 1