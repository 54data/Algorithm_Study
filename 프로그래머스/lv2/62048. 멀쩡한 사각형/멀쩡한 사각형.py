def solution(w,h):
    if w == h:
        answer = w*h - w
    else:
        a, b = max(w, h), min(w, h)
        while b>0:
            a, b = b, a%b
        answer = w*h - (w+h-a)
    return answer
