# BOJ 2908 상수

A, B = map(str, input().split())
Aa = ''
Bb = ''
for a in A[::-1]:
  Aa += a
for b in B[::-1]:
  Bb += b
Aa = int(Aa)
Bb = int(Bb)
if Aa > Bb:
  print(Aa)
else:
  print(Bb)