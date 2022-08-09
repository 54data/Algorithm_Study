from bisect import bisect_right, bisect_left

def cnt_index(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = cnt_index(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = cnt_index(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
        
    return answer