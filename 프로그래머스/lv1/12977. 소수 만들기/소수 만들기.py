def solution(nums):
    from itertools import combinations as cb
    cb_list = list(cb(nums, 3))
    cnt = 0
    for i in cb_list:
        check_num = sum(i)
        for x in range(2, check_num+1):
            if (check_num % x == 0) and (check_num != x): break
            elif check_num == x: cnt += 1
    return cnt