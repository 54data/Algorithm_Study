def solution(s):
    if s[0] == ')' :
        return False
    a = [s[0]]
    for i in s[1:]:
        if a != []:
            if a[-1] == '(' and i == ')':
                a.pop(-1)
                continue
        a.append(i)

    return True if a == [] else False