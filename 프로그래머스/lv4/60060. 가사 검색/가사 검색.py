from bisect import bisect_left, bisect_right
from collections import defaultdict
def solution(words, queries):
    words.sort()
    reverse_words = sorted(list(map(lambda x:x[::-1], words)))
    word_dict = defaultdict(list)
    reverse_dict = defaultdict(list)
    
    for i in range(len(words)):
        word_dict[len(words[i])].append(words[i])
        reverse_dict[len(reverse_words[i])].append(reverse_words[i])
    
    answer = []
    
    for i in range(len(queries)):
        cnt = 0
        len_ = len(queries[i])

        if queries[i][0] == queries[i][-1]:
            answer.append(len(word_dict[len_]))
            continue
        
        elif queries[i][-1] == '?':
            a = bisect_left(word_dict[len_], queries[i].replace('?', 'a'))
            b = bisect_right(word_dict[len_], queries[i].replace('?', 'z'))

        else:
            reverse_i = queries[i][::-1]
            a = bisect_left(reverse_dict[len_], reverse_i.replace('?', 'a'))
            b = bisect_right(reverse_dict[len_], reverse_i.replace('?', 'z'))

        answer.append(b-a)         
            
    return answer