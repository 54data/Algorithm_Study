import math
N, K = map(int, input().split())
answer = []

for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        answer.append(i)

for j in answer:
    if N//j not in answer:
        answer.append(N//j)

answer.sort()
if K-1 >= len(answer) :
    print(0)
else:
    print(answer[K-1])