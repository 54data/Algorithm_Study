n = int(input())
answer = 0
nlist = list(map(int, input().split()))

for j in nlist:
    if j != 0 and j != 1:
        for x in range(2, int(j**0.5)+1):
            if j%x == 0 and j!=x:
                break
        else:
            answer += 1
        
print(answer)