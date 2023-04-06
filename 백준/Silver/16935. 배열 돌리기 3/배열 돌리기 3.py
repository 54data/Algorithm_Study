n, m, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

num_list = list(map(int, input().split()))

for i in num_list:
    if i == 1:
        graph = graph[::-1]
    if i == 2:
        graph = list(map(lambda x:x[::-1], graph))
    if i == 3:
        right_list = []
        for j in range(len(graph[0])):
            right_list.append(list(map(lambda x:x[j], graph))[::-1])
        graph = right_list
    if i == 4:
        left_list = []
        for j in range(len(graph[0])-1, -1, -1):
            left_list.append(list(map(lambda x:x[j], graph)))
        graph = left_list
    if i == 5:
        fifth_list = []
        a = len(graph)//2
        b = len(graph[0])//2
        for j in range(a):
            fifth_list.append(graph[j+a][:b] + graph[j][:b])
        for j in range(a):
            fifth_list.append(graph[j+a][b:] + graph[j][b:])
        graph = fifth_list
    if i == 6:
        six_list = []
        a = len(graph)//2
        b = len(graph[0])//2
        for j in range(a):
            six_list.append(graph[j][b:] + graph[j+a][b:])
        for j in range(a):
            six_list.append(graph[j][:b] + graph[j+a][:b])
        graph = six_list
        
for x in graph:
    for y in x:
        print(y, end=' ')
    print(end='\n')