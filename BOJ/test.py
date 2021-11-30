import sys

N = int(input())


def solution():
    dp = [-1] * (N + 1)

    dp[0] = 0
    dp[1] = 1

    for n in range(2, N + 1):
        dp[n] = sys.maxsize
        for k in range(1, int(n ** 0.5) + 1):
            dp[n] = min(dp[n], dp[n - k**2] + 1)

    return dp[N]


print(solution())