s = input()
slist = []
split_s = s[0]
for i in s[1:]:
    if i == split_s[-1]:
        split_s += i
    else:
        slist.append(split_s)
        split_s = i

slist.append(split_s)
cnt = 0
  
while True:
    if ''.join(slist).count('1') == len(s) or ''.join(slist).count('0') == len(s):
        break
    if sum(map(lambda x:'0' in x, slist)) <= sum(map(lambda x:'1' in x, slist)):
        for i in range(len(slist)):
            if '0' in slist[i]:
                slist[i] = slist[i].replace('0', '1')
                break

    else:
        for i in range(len(slist)):
            if '1' in slist[i]:
                slist[i] = slist[i].replace('1', '0')
                break
    cnt += 1

print(cnt)