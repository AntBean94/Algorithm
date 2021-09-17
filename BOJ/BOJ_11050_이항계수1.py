# BOJ 11050 이항 계수 1

N, K = map(int, input().split())
ans = 1
for i in range(K + 1, N + 1):
    ans *= i
for i in range(2, N - K + 1):
    ans //= i
print(ans)