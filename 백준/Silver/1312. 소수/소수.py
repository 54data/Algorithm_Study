a, b, c = map(int, input().split())

a = a%b

if a == 0:
    print(0)
else:
    for i in range(c-1):
        a = (a*10)%b
    print((a*10)//b)