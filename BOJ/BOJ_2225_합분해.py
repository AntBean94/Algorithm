# BOJ 2225 합분해

'''
조건 1.
(1, 2) != (2, 1)
조건 2.
0 이상의 정수로 구성
조건 3.
1,000,000,000 으로 나눈 나머지를 출력

점화식
DP[i][j] = sum(DP[i-1][:j+1])
'''

N, K = map(int, input().split())
DP = [[1] * (N + 1) for _ in range(K)]
for i in range(1, K):
    for j in range(N + 1):
        DP[i][j] = sum(DP[i-1][:j+1])
print(DP[K-1][N] % 1000000000)