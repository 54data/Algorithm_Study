from collections import deque
from collections import defaultdict

def solution(tickets):
    tickets.sort(key=lambda x:(x[1], x[0]))
    path_dict = defaultdict(list)
    answer = []
    
    for [x, y] in tickets:
        path_dict[x].append(y)
        
    for x in path_dict.keys():
        path_dict[x].sort(reverse=True)
        
    def dfs():
        stack = ["ICN"]
        while stack:
            start = stack[-1]
            if path_dict[start]:
                stack.append(path_dict[start].pop())
            else:
                answer.append(stack.pop())
    
    dfs()
    return answer[::-1]