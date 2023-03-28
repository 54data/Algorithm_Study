n = int(input())
b = list(map(int, input().split()))
mi, ma = map(str, [min(b), max(b)])
print(mi, ma)