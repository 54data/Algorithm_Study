from itertools import product
def solution(word):
    alist = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(1, 6):
        result += list(product(alist, repeat=i))
    result.sort()
    result = list(map(lambda x:''.join(x), result))
    return result.index(word) + 1