# BOJ 10845 큐

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque()
cnt = 0
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push': num = int(cmd[1])
    cmd = cmd[0]
    if cmd == 'push': 
        Q.append(num)
        cnt += 1
    elif cmd == 'pop':
        if Q: 
            print(Q.popleft())
            cnt -= 1
        else: print(-1)
    elif cmd == 'size': print(cnt)
    elif cmd == 'empty':
        if cnt: print(0)
        else: print(1)
    elif cmd == 'front':
        if cnt: print(Q[0])
        else: print(-1)
    elif cmd == 'back':
        if cnt: print(Q[-1])
        else: print(-1)