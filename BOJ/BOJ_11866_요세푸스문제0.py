# BOJ 11866 요세푸스 문제 0

from collections import deque
N, K = map(int, input().split())
Q = deque([i for i in range(1, N + 1)])
seq = []
while Q:
    for k in range(K-1):
        n = Q.popleft()
        Q.append(n)
    seq.append(Q.popleft())
print(f'<{", ".join(map(str, seq))}>')