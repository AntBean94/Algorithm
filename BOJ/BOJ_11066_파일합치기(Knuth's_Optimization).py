# BOJ 11066 파일 합치기 (Knuth's Optimization)

'''
Knuth's Optimization

조건 1)
점화식: DP[i][j] = min(DP[i][k] + DP[k + 1][j]) + C[i][j] (i <= k < j)

조건 2)
사각 부등식: C[a][c] + C[b][d] <= C[a][d] + C[b][c] (a <= b <= c <= d)

조건 3)
단조성: C[b][c] <= C[a][d] (a <= b <= c <= d)

위의 조건을 만족할 때 C에 대해
A[i][j]가 DP[i][j]가 최소값이 되게하는 k(i < k < j)값을 저장하는 배열이라면,
다음이 성립한다.

A[i][j-1] < A[i][j] < A[i+1][j]

따라서 최솟값을 결정하는 k를 찾는데 걸리는 시간이 N에서 상수시간으로 
바뀌면 시간복잡도를 O(N^3) => O(N^2) 로 줄일 수 있다.
'''

import sys
input = sys.stdin.readline

INF = 100000000
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    files = list(map(int, input().split()))
    cum = [0] * (N + 1)
    for i in range(1, N + 1):
       cum[i] += cum[i - 1] + files[i - 1]
    # dp 테이블
    DP = [[0] * (N + 1) for _ in range(N + 1)]
    # k 최적해 보관
    A = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        A[i][i] = i
    
    # 간격
    for d in range(1, N):
        for l in range(1, N - d + 1):
            r = l + d
            DP[l][r] = INF
            for k in range(A[l][r-1], A[l+1][r] + 1):
                if DP[l][k] + DP[k + 1][r] + cum[l] - cum[r - 1] < DP[l][r]:
                    DP[l][r] = DP[l][k] + DP[k + 1][r] + cum[l] - cum[r - 1]
                    A[l][r] = k
    for a in A:
        print(a)
    print()
    
    for d in DP:
        print(d)
    print(DP[1][N])

