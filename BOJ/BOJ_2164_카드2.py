# BOJ 2164 카드2

from collections import deque

N = int(input())
Q = deque([i for i in range(1, N + 1)])

while len(Q) > 1:
    Q.popleft()
    n = Q.popleft()
    Q.append(n)
print(Q[0])
