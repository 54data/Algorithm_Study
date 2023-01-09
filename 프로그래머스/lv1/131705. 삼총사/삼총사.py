from itertools import combinations

def solution(number):
    comb = list(combinations(number, r=3))
    nums_list = [nums for nums in comb if sum(nums)==0]
    return len(nums_list)