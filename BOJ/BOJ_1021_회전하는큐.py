# BOJ 1021 회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

# 뽑는 원소를 중심으로 양쪽의 거리가 같으므로 그리디하게 접근
N, M = map(int, input().split())
arr = list(map(int, input().split()))
Q = deque([i for i in range(1, N + 1)])
ans = 0
l = N
for a in arr:
    dist = 0
    for i in range(l):
        if a == Q[i]:
            if i < abs(i - l):
                dist = i
            else: dist = i - l
    ans += abs(dist)
    while dist:
        if dist > 0:
            n = Q.popleft()
            Q.append(n)
            dist -= 1
        else:
            n = Q.pop()
            Q.appendleft(n)
            dist += 1
    Q.popleft()
    l -= 1
print(ans)