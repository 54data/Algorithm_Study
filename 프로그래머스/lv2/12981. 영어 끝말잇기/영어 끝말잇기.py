def solution(n, words):
    answer = []
    cnt = 1
    for idx, word in enumerate(words):
        if idx != 0:
            if ((word[0] != words[idx-1][-1])) or (word in words[:idx]):
                answer.append((idx % n)+1)
                answer.append(cnt)
                break
        if (idx+1) % n == 0:
            cnt += 1
        
    return answer if answer else [0,0]