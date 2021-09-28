# BOJ 9012 괄호

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    answer = 'YES'
    S = input().rstrip()
    stack = []
    for s in S:
        if s == '(': stack.append(s)
        else:
            if not stack:
                answer = 'NO'
                break
            else:
                stack.pop()
    if stack: answer = 'NO'
    print(answer)