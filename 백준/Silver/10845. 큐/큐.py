from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if len(a) == 2:
        queue.append(int(a[1]))
    elif len(a) == 1:
        if a[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif a[0] == 'size':
            print(len(queue))
        elif a[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif a[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif a[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)