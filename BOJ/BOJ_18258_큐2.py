# BOJ 18258 큐 2

from collections import deque
import sys
input = sys.stdin.readline

Q = deque()
N = int(input())
cnt = 0
for i in range(N):
    info = list(map(str, input().split()))
    if info[0] == 'push':
        Q.append(int(info[1]))
        cnt += 1
    elif info[0] == 'pop':
        if cnt: 
            print(Q.popleft())
            cnt -= 1
        else: print(-1)
    elif info[0] == 'size':
        print(cnt)
    elif info[0] == 'empty':
        if cnt: print(0)
        else: print(1)
    elif info[0] == 'front':
        if cnt: print(Q[0])
        else: print(-1)
    else:
        if cnt: print(Q[-1])
        else: print(-1)