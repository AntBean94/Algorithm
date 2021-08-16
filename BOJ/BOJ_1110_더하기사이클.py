# BOJ 1110 더하기 사이클

N = int(input())
K = 1000
cnt = 0
while N!=K:
  if K==1000:
    K = N
  if K < 10:
    K = '0' + str(K)
  else:
    K = str(K)
  T = int(K[1])
  K = int(str(K)[0]) + T
  K = str(T) + str(K)[-1]
  K = int(K)
  cnt += 1
print(cnt)
  