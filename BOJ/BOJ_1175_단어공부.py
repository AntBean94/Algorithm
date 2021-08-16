# BOJ 1175 단어공부

char = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 
  'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 
  'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq',
  'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww',
  'Xx', 'Yy', 'Zz']

ans = [0] * len(char)
for i in input():
  for c in range(len(char)):
    if i in char[c]:
      ans[c] += 1

mx = 0
sm = 0
for a in ans:
  if a > mx:
    mx = a
    sm = 0
  elif a==mx:
    sm += 1

if sm > 0:
  print('?')
else:
  print(char[ans.index(mx)][0])
