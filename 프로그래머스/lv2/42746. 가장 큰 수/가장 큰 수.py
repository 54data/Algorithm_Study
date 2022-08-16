def check(n):
    if len(n) == 1:
        return n*6
    else:
        return n*3
    
def solution(numbers):
    numbers = list(map(lambda x:str(x), numbers))
    numbers = sorted(numbers, key=lambda x:int(check(x)[:6]), reverse=True)
    
    answer = ''.join(numbers)
    
    if int(answer) != 0:
        return answer
    else:
        return '0'
