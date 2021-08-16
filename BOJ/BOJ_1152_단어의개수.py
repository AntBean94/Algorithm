# BOJ 1152 단어의 개수

cnt = 0
chk = 0
for i in input():
  if i!=" ":
    if chk==0:
      cnt += 1
    chk += 1
  else:
    chk = 0
print(cnt)
  
