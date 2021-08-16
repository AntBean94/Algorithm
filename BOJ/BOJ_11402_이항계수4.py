# BOJ 11402 이항계수 4


N, K, M = map(int, input().split())

# sol = N!/K!(N-K)!
a = 1
for i in range(N-K+1, N+1):
  a *= i
  print(a)
b = 1
for i in range(1, N-K):
  b *= i

print((a/b))