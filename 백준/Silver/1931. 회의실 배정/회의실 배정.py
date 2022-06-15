n = int(input())
n_list = []
for i in range(n):
    start, end = map(int, input().split())
    n_list.append((start, end))
    
n_list.sort(key = lambda x: x[0])
n_list.sort(key = lambda x: x[1])

cnt = 0
end_time = 0
for i, x in n_list:
    if end_time <= i:
        end_time = x
        cnt += 1

print(cnt)