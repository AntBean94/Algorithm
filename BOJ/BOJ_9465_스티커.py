# BOJ 9465 스티커

'''
DP[i][j] = max(바로 전 반대, 2개전 반대)
DP[i][j] = max(DP[R[i]][j-1], DP[R[i]][j-2]) + S[i][j]
'''
R = [1, 0]
T = int(input())
for tc in range(T):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * (N + 1) for _ in range(2)]
    # 초기화
    DP[0][1], DP[1][1] = S[0][0], S[1][0]
    # bottom-up
    for j in range(2, N + 1):
        for i in range(2):
            DP[i][j] = max(DP[R[i]][j-1], DP[R[i]][j-2]) + S[i][j-1]
    print(max(DP[0][N], DP[1][N]))