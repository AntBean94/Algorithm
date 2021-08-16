# BOJ 2675 문자열 반복

for _ in range(int(input())):
  n, text = map(str, input().split())
  ans = ''
  for t in text:
    for i in range(int(n)):
      ans += t
  print(ans)
