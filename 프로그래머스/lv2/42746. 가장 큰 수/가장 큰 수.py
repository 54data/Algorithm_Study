def solution(numbers):
    def len_str(x):
        if len(x) == 1: return x*6
        else: return x*3
    
    numbers = list(map(lambda x:str(x), numbers))
    numbers.sort(key=lambda x:int(len_str(x)[:6]), reverse=True)
        
    answer = ''.join(numbers)
    if int(answer) != 0:
        return answer
    else:
        return '0'