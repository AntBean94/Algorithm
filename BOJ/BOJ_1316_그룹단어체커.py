# BOJ 1316 그룹 단어 체커

ans = 0
for _ in range(int(input())):
  N = input()
  check = []
  pre = ''
  isok = True
  for n in N:
    if n in check and n!=pre:
      isok = False
    pre = n
    check.append(n)
  if isok:
    ans += 1
print(ans)