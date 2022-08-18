n = int(input())
for _ in range(n):
    a = input()
    set_a = list(dict.fromkeys(a))
    for i in set_a:
        a = a.lstrip(i)
    if len(a) != 0:
        n -= 1
    
print(n)