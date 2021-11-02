# BOJ 1935 후위 표기식2

from collections import deque
import sys
input = sys.stdin.readline

alpa = set(i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
idx = {}
N = int(input())
Q = deque()
post_expr = input().rstrip()
for i in post_expr:
    if i in alpa: Q.append(i)
for i in range(len(Q)):
    n = Q.popleft()
    if not n in idx:
        idx[n] = int(input())
for i in post_expr:
    if i in alpa: Q.append(idx[i])
    else:
        b = Q.pop()
        a = Q.pop()
        if i == "*": Q.append(a * b)
        elif i == "/": Q.append(a / b)
        elif i == "+": Q.append(a + b)
        else: Q.append(a - b)
print("%.2f" %Q.pop())
