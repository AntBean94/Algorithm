# BOJ 1929 소수구하기(다시풀기)

M, N = map(int, input().split())

arr = [True] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
  for j in range(2, N//2+1):
    if i * j > N:
      break
    else:
      arr[i * j] = False
for i in range(M, len(arr)):
  if arr[i] and i > 1:
    print(i)

