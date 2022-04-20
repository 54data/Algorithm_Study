num = list(map(int, input()))
num = list(map(str, sorted(num, reverse=True)))
result = ''
result = result.join(num)
print(result)