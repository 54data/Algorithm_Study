def leng(numbers):
    if len(numbers) == 1:
        return numbers * 6
    else:
        return numbers * 3
    
def solution(numbers):
    numbers = list(map(lambda x:str(x), numbers))
    numbers = sorted(numbers, key=lambda x:int(leng(x)[:4]), reverse=True)
    answer = ''.join(numbers) 
    return answer if int(answer) != 0 else '0'