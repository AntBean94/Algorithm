# BOJ 17404 RGB거리 2

'''
규칙
1. 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
3. i(2 <= i <= N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

방법
1. 처음부터 시작색을 고정하고 최솟값을 구한다.
 - 즉 r, g, b 각각의 색으로 출발하는 경우의 최솟값을 각각 구한다.
2. 최솟값 구하는 방법은 DP
'''
import sys
input = sys.stdin.readline

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
ans = 1000001
for n in range(3):
    T = [[1000001] * 3 for _ in range(N)]
    T[0][n] = C[0][n]
    for i in range(1, N):
        for j in range(3):
            for k in range(3):
                if i == N - 1:
                    if j != k and j != n:
                        T[i][j] = min(T[i][j], T[i-1][k] + C[i][j])
                else:
                    if j != k:
                        T[i][j] = min(T[i][j], T[i-1][k] + C[i][j])
    ans = min(ans, min(T[-1]))
print(ans)