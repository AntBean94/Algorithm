# BOJ 4344 평균은 넘겠지

for _ in range(int(input())):
  arr = list(map(int, input().split()))
  total = 0
  for n in arr[1:]:
    total += n
  avg = total / arr[0]
  cnt = 0
  for n in arr[1:]:
    if n > avg:
      cnt += 1
  ans = cnt / arr[0] * 100
  print('{:.3f}%'.format(ans))