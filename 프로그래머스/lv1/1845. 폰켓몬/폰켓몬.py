def solution(nums):
    uniq = len(list(set(nums)))
    if uniq > len(nums)//2:
        uniq = len(nums)//2
    return uniq