# BOJ 1966 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    for i in range(len(arr)):
        Q.append([arr[i], i])
    n = arr[M]
    cnt = 0
    while True:
        cnt += 1
        # 최댓값 확인
        m = max(Q)
        m = m[0]
        t = -1
        while True:
            q = Q.popleft()
            if m == q[0]:
                t = q[1]
                break
            else: Q.append(q)
        if t == M: break
    print(cnt)