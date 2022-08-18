def solution(people, limit):
    reverse_list = sorted(people, reverse=True)
    people.sort()
    save_cnt1 = 0
    save_cnt2 = 0
    live = 0
    answer = 0
    while live < len(people):
        if reverse_list[save_cnt1] + people[save_cnt2] <= limit:
            save_cnt1, save_cnt2, answer = save_cnt1+1, save_cnt2+1, answer+1
            live += 2
        else:
            save_cnt1, answer = save_cnt1+1,  answer+1
            live += 1
    return answer