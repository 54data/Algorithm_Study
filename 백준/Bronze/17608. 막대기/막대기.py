import sys
nlist = []
n = int(sys.stdin.readline()) # 막대의 갯수

for _ in range(n):
    nlist.append(int(sys.stdin.readline()))
    
result = []
a = nlist.pop()
result.append(a)

for i in nlist[::-1]:
    if i <= a:
        nlist.pop()
    elif i > a:
        a = nlist.pop()
        result.append(a)
            
print(len(result))