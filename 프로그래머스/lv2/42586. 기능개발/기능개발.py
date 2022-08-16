def solution(progresses, speeds):
    result = []
    while progresses != []:
        cnt = 0
        num = len(progresses)
        for i in range(num):
            progresses[i] += speeds[i]
        while True:
            if progresses[0] >= 100:
                x = progresses.pop(0)
                del speeds[0]
                cnt += 1
                if len(progresses) == 0:
                    result.append(cnt)
                    break
                continue
            elif cnt != 0:
                result.append(cnt)
                break
            else:
                break

    return result