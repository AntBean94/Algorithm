# BOJ 2294 동전 2

'''
점화식
DP[N] = min(DP[N], DP[N-a] + 1)
'''

N, K = map(int, input().split())
coin = sorted(list(set(int(input()) for _ in range(N))))
DP = [0] + [1000000000] * K
for c in coin:
    for i in range(c, K + 1):
        if not (i - c) or DP[i - c]:
            DP[i] = min(DP[i], DP[i - c] + 1)
if DP[-1] == 1000000000: print(-1)
else: print(DP[-1])