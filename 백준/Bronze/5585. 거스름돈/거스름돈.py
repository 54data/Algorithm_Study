N = int(input())
coin_type = [500, 100, 50, 10, 5, 1]
out_n = 1000 - N
cnt = 0

for i in coin_type:
    cnt += out_n // i
    out_n %= i
    
print(cnt)
