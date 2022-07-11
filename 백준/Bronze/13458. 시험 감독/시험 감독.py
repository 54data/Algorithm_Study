N = int(input())
Ai = list(map(int, input().split()))

B, C = map(int, input().split())

Ai = list(map(lambda x: x-B if x-B > 0 else 0, Ai))

result = len(Ai)

for i in Ai:
    result += i//C
    i %= C
    if (i>0) and (i<C):
        result += 1
        
print(result)