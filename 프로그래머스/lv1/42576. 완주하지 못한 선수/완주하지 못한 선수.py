def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    while True:
        x = participant.pop()
        y = completion.pop()
        if x == y:
            pass
        else:
            return x
        if completion == []:
            return participant[0]
            