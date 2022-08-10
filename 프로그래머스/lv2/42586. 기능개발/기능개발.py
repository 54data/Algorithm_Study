
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(progresses, speeds):
    result = []
    for i, x in zip(progresses, speeds):
        if (100 - i) % x == 0:
            result.append((100 - i) // x)
        else:
            result.append(((100 - i) // x) + 1)

    a = result[0]
    answer = []
    cnt = 1
    for i in range(1, len(result)):
        if result[i] <= a:
            cnt += 1
        else:
            a = result[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer
