def change(s):
    new_s = ''
    while True:
        new_s = str(s%2) + new_s
        s = s//2
        if s == 0:
            return new_s

def solution(s):
    cnt = 0
    zero_cnt = 0
    while True:
        zero_cnt += s.count('0')
        s = len([i for i in list(s) if i!='0'])
        s = change(s)
        cnt += 1
        if s == '1':
            break
        
    return [cnt, zero_cnt]