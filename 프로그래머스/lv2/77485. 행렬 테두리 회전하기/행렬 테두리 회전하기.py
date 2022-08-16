def solution(rows, columns, queries):
    x = 1
    graph = []
    for i in range(rows):
        nlist = []
        for j in range(columns):
            nlist.append(x)
            x += 1
        graph.append(nlist)
            
    result = []
    for q in queries:
        min_cnt = 1e9
        temp = []

        for i in range(q[1]-1, q[3]-1):
            if i == q[1]-1:
                temp.append(graph[q[0]-1][i+1])
                graph[q[0]-1][i+1] = graph[q[0]-1][i]
                min_cnt = min(min_cnt, min(temp))
            else:
                temp.append(graph[q[0]-1][i+1])
                min_cnt = min(min_cnt, min(temp))
                graph[q[0]-1][i+1] = temp.pop(0)

        for i in range(q[0]-1, q[2]-1): 
            temp.append(graph[i+1][q[3]-1])
            min_cnt = min(min_cnt, min(temp))
            graph[i+1][q[3]-1] = temp.pop(0)
                            
        for i in range(q[3]-1, q[1]-1, -1):
            temp.append(graph[q[2]-1][i-1])
            min_cnt = min(min_cnt, min(temp))
            graph[q[2]-1][i-1] = temp.pop(0)
                        
        for i in range(q[2]-1, q[0]-1, -1):
            temp.append(graph[i-1][q[1]-1])
            min_cnt = min(min_cnt, min(temp))
            graph[i-1][q[1]-1] = temp.pop(0)
            
        result.append(min_cnt)
    return result