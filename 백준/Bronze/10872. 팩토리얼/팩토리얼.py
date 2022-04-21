from functools import reduce
num = int(input())
if num == 0:
    print(1)
else:
    num_list = list(range(1, num+1))
    print(reduce(lambda x, y:x*y, num_list))