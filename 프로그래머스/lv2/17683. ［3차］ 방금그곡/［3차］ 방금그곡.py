def change(s):
    nlist = ['C#', 'D#', 'F#', 'G#', 'A#']
    clist = ['1', '2', '3', '4', '5']
    
    for i in range(5):
        if nlist[i] in s:
            s = s.replace(nlist[i], clist[i])
            
    return s

def solution(m, musicinfos):
    answer = ''
    m = change(m)
    cnt = 0
    max_play = [0]
    for i in musicinfos:
        i = i.split(',')
        i[-1] = change(i[-1])
        
        time = (int(i[1][:2]) - int(i[0][:2]))*60 + (int(i[1][3:]) - int(i[0][3:]))
        play = len(i[-1])
        real_play = i[-1] * (time // play) + i[-1][:time%play]

        if m in real_play:
            if cnt == 0:
                answer = i[-2]
                max_play[0] = time
            else:
                if max_play[0] < time:
                    answer = i[-2]
                    max_play[0] = time
            cnt += 1
        
    return answer if answer != '' else "(None)"

