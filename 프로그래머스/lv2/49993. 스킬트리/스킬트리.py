def solution(skill, skill_trees):
    answer = 0
    for x in skill_trees:
        non_skill = True
        result = [-1]
        for i in x:
            if i in skill:
                non_skill = False
                if skill.index(i) - 1 == result[0]:
                    result[0] = skill.index(i)
                else:
                    result[0] = -1
                    break
            else:
                non_skill = True
                
        if result[0] == -1 and non_skill == True:
            answer += 1
        if result[0] != -1:
            answer += 1
            
    return answer