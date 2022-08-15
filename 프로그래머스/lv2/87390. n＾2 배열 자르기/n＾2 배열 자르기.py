def solution(n, left, right):
    graph = []
    for i in range(left, right+1):
        graph.append(max(i%n, int(i/n)) + 1)
    
    return graph

