# BOJ 10828 스택

import sys
input = sys.stdin.readline

N = int(input())
stack = []
cnt = 0
for i in range(N):
    info = list(map(str, input().split()))
    message = info[0]
    if message == "push":
        stack.append(info[1])
        cnt += 1
    elif message == "pop":
        if cnt:
            print(stack.pop())
            cnt -= 1
        else: print(-1)
    elif message == "size":
        print(cnt)
    elif message == "empty":
        if cnt: print(0)
        else: print(1)
    elif message == "top":
        if cnt: print(stack[-1])
        else: print(-1)
