from collections import defaultdict
def solution(record):
    id_list = defaultdict(list)
    result = []
    for comm in record:
        i = comm.split()
        if i[0] == 'Enter':
            id_list[i[1]].append(i[2])
            result.append('{0}님이 들어왔습니다.'.format(i[1]))
        elif i[0] == 'Change':
            id_list[i[1]][-1] = i[2]
        else:
            result.append('{0}님이 나갔습니다.'.format(i[1]))
            
    for i in range(len(result)):
        a = result[i].split('님')
        result[i] = f'{id_list[a[0]][-1]}님'+a[1]
    return result

            
        
        
        