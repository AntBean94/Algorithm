<<<<<<< HEAD
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
=======
a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i)
a = b
b[2] = 100
print(a, b)
>>>>>>> 0e8f066209fe0511517b80b43043f210da524bfd
