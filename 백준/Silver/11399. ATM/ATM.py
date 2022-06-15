n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

cnt = 0
out_list = []
for i in n_list:
    cnt += i
    out_list.append(cnt)
    
print(sum(out_list))