# BOJ 10866 덱

from collections import deque
import sys
input = sys.stdin.readline

D = deque()
N = int(input())
cnt = 0
for i in range(N):
    info = list(map(str, input().split()))
    cmd = info[0]
    if cmd == 'push_front':
        D.appendleft(int(info[1]))
        cnt += 1
    elif cmd == 'push_back':
        D.append(int(info[1]))
        cnt += 1
    elif cmd == 'pop_front':
        if cnt: 
            print(D.popleft())
            cnt -= 1
        else: print(-1)
    elif cmd == 'pop_back':
        if cnt: 
            print(D.pop())
            cnt -= 1
        else: print(-1)
    elif cmd == 'size':
        print(cnt)
    elif cmd == 'empty':
        if cnt: print(0)
        else: print(1)
    elif cmd == 'front':
        if cnt: print(D[0])
        else: print(-1)
    elif cmd == 'back':
        if cnt: print(D[-1])
        else: print(-1)