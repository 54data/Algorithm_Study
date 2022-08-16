def solution(n):
    nlist = ['1', '2', '4']
    num = ''
    while n!=0:
        if n % 3 != 0:
            num += str(n%3)
            n //= 3
            print(num)
        else:
            num += nlist[-1]
            n = n//3 -1
            print(num)
            
    return num[::-1]