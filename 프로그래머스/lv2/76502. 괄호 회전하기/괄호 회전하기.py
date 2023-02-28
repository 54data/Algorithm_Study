def solution(s):
    str_dict = {"(":")", "[":"]", "{":"}"}
    answer = 0
    
    for i in range(len(s)):
        stack = []
        for j in s[i:]+s[:i]: # 회전된 문자열
            if stack and stack[-1] in str_dict.keys() and str_dict[stack[-1]] == j:
                    stack.pop()
            else:
                stack.append(j)
        if stack == []:
            answer += 1
    
    return answer
                    
                    
            