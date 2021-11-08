# Leetcode 62 Unique Paths

m, n = map(int, input().split())

# 1. DP
DP = [[0] * n for _ in range(m)]
DP[0][0] = 1
for i in range(m):
    for j in range(n):
        if j + 1 < n: DP[i][j + 1] += DP[i][j]
        if i + 1 < m: DP[i + 1][j] += DP[i][j]
print(DP[m-1][n-1])

# 2. Math - 경우의 수
def f(x, y = 1):
    if x == y: return 1
    return x * f(x - 1, y)

cal = lambda x, y: f(x + y, max(x, y)) / f(min(x, y))
print(1 if m == 1 or n == 1 else int(cal(m - 1, n - 1)))