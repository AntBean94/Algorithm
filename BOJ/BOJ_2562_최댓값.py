# BOJ 2562 최댓값

check = 0
maxnum = 0
for i in range(9):
  t = int(input())
  if t > maxnum:
    maxnum = t
    check = i + 1
print(maxnum)
print(check)
