# BOJ 2618 경찰차

'''

초기상황
경찰차1 = (1, 1)
경찰차2 = (N, N)

점화식
DP[A][B] = min(DP[X][B] + dist(A, X), DP[A][X] + dist(B, X))
A, B는 각각 최근 해결한 사건의 번호
사건의 번호로 위치좌표를 얻을 수 있음

=> 최종적으로 DP행렬의 W번째 행과 열의 값중 가장 작은 값을 출력

경로
재귀로 해결

출력
첫째 줄에 이동한 총거리
둘째 줄부터 사건이 맡겨진 경찰처 번호
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
INF = 1000000000

def dist(l1, l2):
    if l1 == 0: x1, y1 = 1, 1
    else: x1, y1 = loc[l1]
    if l2 == 0: x2, y2 = N, N
    else: x2, y2 = loc[l2]
    return abs(x1 - x2) + abs(y1 - y2)

N = int(input())
W = int(input())
loc = [0] + [list(map(int, input().split())) for _ in range(W)]
DP = [[INF] * (W + 1) for _ in range(W + 1)]
DP[0][0] = 0
# 최단거리 계산
for i in range(W):
    for j in range(W):
        n = max(i, j) + 1   # 사건 번호
        if i == n or j == n: continue # 같은 사건을 함께 처리할 수는 없음
        DP[n][j] = min(DP[n][j], DP[i][j] + dist(i, n))
        DP[i][n] = min(DP[i][n], DP[i][j] + dist(n, j))
# 최단거리 출력
min_dist = INF
min_loc = [0, 0]
for i in range(W):
    if DP[i][W] < min_dist:
        min_loc = [i, W]
        min_dist = DP[i][W]
    if DP[W][i] < min_dist:
        min_loc = [W, i]
        min_dist = DP[W][i]
print(min_dist)

# 최단거리 역추적
def make_route(n, min_loc):
    if n == 0: return
    a, b = min_loc
    # 1일 때
    if a == n:
        for i in range(n-1, -1, -1):
            if i == b: continue
            # 같은 조건
            if dist(i, n) == DP[n][b] - DP[i][b]:
                make_route(n-1, [i, b])
                break
        print("1")
    # 2일 때
    else:
        for i in range(n-1, -1, -1):
            if i == a: continue
            if dist(n, i) == DP[a][n] - DP[a][i]:
                make_route(n-1, [a, i])
                break
        print("2")

make_route(W, min_loc)