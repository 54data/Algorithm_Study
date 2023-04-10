import sys
from itertools import combinations

N, K = map(int, input().split())
if K < 5:
    print(0)
    sys.exit()

word_list = [input().strip()[4:-4] for _ in range(N)]
temp = {'a', 'n', 't', 'i', 'c'}
chars = [chr(ord('a')+i) for i in range(26) if chr(ord('a')+i) not in temp]

max_cnt = -1
for comb in combinations(chars, K-5):
    temp_comb = temp | set(comb)
    cnt = 0
    for word in word_list:
        for i in range(len(word)):
            if word[i] not in temp_comb:
                break
        else:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

if max_cnt != -1:
    print(max_cnt)
else:
    print(0)