# BOJ 1065 한수

N = int(input())
cnt = 0
for i in range(1, N+1):
  if len(str(i))<=2:
    cnt += 1
  else:
    check = int(str(i)[0]) - int(str(i)[1])
    pre = int(str(i)[0])
    t = 0
    for j in str(i)[1:]:
      c = pre - int(j)
      if c!=check:
        break
      t += 1
      pre = int(j)
    if t==len(str(i))-1:
      cnt += 1
print(cnt)
      