# BOJ 1931 회의실 배정

import sys
input = sys.stdin.readline

# 끝나는 시간 기준 정렬
# 그중에 가능한 놈으로!

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
print(arr)

ans = 0
prev = 0
for i in range(N):
    if arr[i][0] >= prev:
        prev = arr[i][1]
        ans += 1
print(ans)