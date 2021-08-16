# BOJ 2941 크로아티아 알파벳

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
i = 0
cnt = 0
while i < len(N):
  if i < len(N)-2:
    if N[i:i+3] in cro:
      cnt += 1
      i += 3
    elif N[i:i+2] in cro:
      cnt += 1
      i += 2
    else:
      cnt += 1
      i += 1
  elif i < len(N)-1:
    if N[i:i+2] in cro:
      cnt += 1
      i += 2
    else:
      cnt += 1
      i += 1
  else:
    cnt += 1
    i += 1
print(cnt)
    