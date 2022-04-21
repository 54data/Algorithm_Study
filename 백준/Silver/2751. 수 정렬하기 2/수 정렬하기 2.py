import sys
num = int(input())
result = sorted([int(sys.stdin.readline()) for _ in range(num)])
for i in result:
    print(i)