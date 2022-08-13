# 암호만들기
from itertools import combinations as cb

l, c = map(int, input().split())
nlist = list(input().split())

result = list(cb(nlist, l))
result = list(map(lambda x:sorted(list(x)), result))
result.sort()

for i in result:
    cnt = i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u')
    if (cnt >= 1) and (cnt <= l-2):
        print(''.join(i))