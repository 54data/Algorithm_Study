n = input()
h = len(n)//2
answer = 'READY'


if sum(map(lambda x:int(x), n[:h])) == sum(map(lambda x:int(x), n[h:])):
    answer = 'LUCKY'
        
print(answer)