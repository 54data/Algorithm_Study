D, m = map(int, input().split())

d = [[0, 0] for _ in range(D+1)]

d[1] = [1, 0]
d[2] = [0, 1]

for i in range(3, D+1):
    d[i] = [d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]
    
for i in range(m//d[D][1], 1, -1):
    new_m = m - d[D][1] * i
    if new_m % d[D][0] == 0:
        answer = new_m // d[D][0]
        if (answer >= 1) and (i >= answer):
            print(answer)
            print(i)
            break