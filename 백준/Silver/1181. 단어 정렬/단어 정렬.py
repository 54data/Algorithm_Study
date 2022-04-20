num = int(input())
a = [input() for _ in range(num)]
a = list(set(a))
a = sorted(a, key=lambda x:(len(x), x))

for i in a:
    print(i)