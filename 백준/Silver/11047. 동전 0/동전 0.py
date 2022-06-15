n, k = map(int, input().split())
n_list = []
for i in range(n):
    num = int(input())
    if num <= k:
        n_list.append(num)
    
n_list.sort(reverse=True)
cnt = 0

for i in n_list:
    if k >= i:
        cnt += k//i
        k = k - i*(k//i)
    if k == 0:
        break
        
print(cnt)