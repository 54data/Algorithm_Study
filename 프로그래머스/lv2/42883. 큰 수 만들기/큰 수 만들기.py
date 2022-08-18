def solution(number, k):
    temp = []
    for i in number:
        while len(temp) > 0 and temp[-1] < i and k > 0:
            temp.pop()
            k -= 1
        temp.append(i)
        
    return ''.join(temp[:len(number)-k])