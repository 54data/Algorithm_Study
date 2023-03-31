x, y = map(int, input().split())
block_list = list(map(int, input().split()))

graph = []

for i in range(x):
    row = []
    for j in range(y):
        if block_list[j] > 0:
            row.append(1)
            block_list[j] -= 1
        else:
            row.append(0)
    graph.insert(0, row)

result = 0

for r in graph:
    cnt = 0
    stack = []
    for c in r:
        if c == 1:
            if stack and stack[-1] == c:
                result += cnt
                cnt = 0
            stack.append(c)
        else:
            if stack and stack[-1] == 1:
                cnt += 1

print(result)