def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x:(x, len(x)))
    answer = False
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[j]) > len(phone_book[i]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return answer
            else:
                break                     
    return True