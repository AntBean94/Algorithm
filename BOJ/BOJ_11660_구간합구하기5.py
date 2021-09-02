# BOJ 11660 구간 합 구하기 5

'''
prefix sum 활용
2차원 배열의 누적합을 구한다.

x1, y1, x2, y2 구간의 합
= (x2, y2) - (x1, y2) - (x2, y1) + (x1, y1)

'''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    line = list(map(int, input().split()))
    # 행 더하기
    for j in range(1, N):
        line[j] = line[j - 1] + line[j]
    # 열에 더하기
    for j in range(1, N + 1):
        arr[i][j] = arr[i - 1][j] + line[j - 1]

for k in arr:
    print(k)
print()
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    ans = arr[x2][y2] - arr[x1][y2] - arr[x2][y1] + arr[x1][y1]
    print(ans)