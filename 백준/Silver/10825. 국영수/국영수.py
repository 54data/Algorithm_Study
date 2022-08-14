n = int(input())
result = []
for _ in range(n):
    name, kor, eng, math = input().split()
    result.append([name, int(kor), int(eng), int(math)])
    
result.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]), reverse=False)

for i in result:
    print(i[0])