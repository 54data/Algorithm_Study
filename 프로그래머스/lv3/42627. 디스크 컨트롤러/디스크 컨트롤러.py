import heapq
def solution(jobs):
    answer = 0
    heap = []
    start = -1
    now = 0
    complete = 0
    job_num = len(jobs)
    
    while complete < job_num:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            min_job = heapq.heappop(heap)
            start = now
            now += min_job[0]
            answer += now - min_job[1]
            complete += 1
        else:
            now += 1
    
    return answer // job_num