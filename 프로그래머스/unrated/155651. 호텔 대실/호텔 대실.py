def change_int(x):
    x_0 = int(x[0][:2])*60 + int(x[0][3:])
    x_1 = int(x[1][:2])*60 + int(x[1][3:]) + 10
    return [x_0, x_1]

def solution(book_time):
    answer = 0
    book_time_int = [change_int(x) for x in book_time]
    t_list = [0] * ((60*24)+10)
    
    for t in book_time_int:
        t_list[t[0]:t[1]+1] = [t_list[x]+1 for x in range(t[0], t[1]+1)]
        t_list[t[1]] -= 1
        
    return max(t_list)