n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
m = len(graph[0])

count = 0

def dfs(x, y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True
    return False

result = 0
clist = []
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            clist.append(count)
            count = 0
            
print(result)
clist.sort()
if result != 0:
    for i in clist:
        print(i)