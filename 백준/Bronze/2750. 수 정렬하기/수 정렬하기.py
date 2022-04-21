import sys
num = int(input())
result = []
for i in range(num):
    a = int(sys.stdin.readline())
    result.append(a)
    
result = sorted(result)
for x in result:
    print(x)