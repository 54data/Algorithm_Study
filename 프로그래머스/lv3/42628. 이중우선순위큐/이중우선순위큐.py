import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    for i in operations:
        a = i.split(' ')
        if a[0] == 'I':
            heapq.heappush(answer, int(a[1]))
        if answer != []:
            if a[0] == 'D':
                if a[1] == '-1':
                    heapq.heappop(answer)
                else:
                    answer = heapq.nlargest(len(answer), answer)[1:]
                    heapq.heapify(answer)
    return [0, 0] if answer == [] else [max(answer), min(answer)]