# BOJ 1874 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
seq = []
for i in range(N):
    seq.append(int(input()))

result = []
stack = []
t = 0
for i in range(1, N+1):
    if i >= seq[t]:
        stack.append(i)
        result.append('+')
        while stack:
            if stack[-1] == seq[t]:
                stack.pop()
                result.append('-')
                t += 1
            elif stack[-1] < seq[t]: break
            else: 
                print('NO')
                exit()
    else:
        stack.append(i)
        result.append('+')
for i in result:
    print(i)